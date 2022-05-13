from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

import os

import moodleXpath
import moodleGetFrom

import time

url_moodle = "https://moodle.tau.ac.il/"
url_moodle_mainscreen = "https://moodle.tau.ac.il/my/"
id_connect_to_moodle = "clicktoconnect"
id_input_username = "Ecom_User_ID"
id_input_personalid = "Ecom_User_Pid"
id_input_password = "Ecom_Password"
id_login = "loginButton2"
id_courses = "nav-drawer"
id_assignment_box = "region-main"
TIMEOUT = 30


def driver_init_login(username, personalid, password,path) -> webdriver.Chrome:

    #### ids


    ### options
    driver_options = webdriver.ChromeOptions()
    driver_options.headless = True
    driver_options.gpu = False
    driver_options.add_experimental_option("prefs", {
    "download.default_directory" : path,
    "download.prompt_for_download": False,
    'profile.default_content_setting_values.automatic_downloads': 2
    })
    desired = driver_options.to_capabilities()
    desired['loggingPrefs'] = { 'performance': 'ALL'}
    service = Service(ChromeDriverManager().install())

    ### init driver
    driver = webdriver.Chrome(service=service, options=driver_options, desired_capabilities=desired)

    ### crawling
    print("Going to moodle")
    driver.get(url_moodle)
    driver.find_element(By.ID, id_connect_to_moodle).click()

    print("Logging in...")
    driver.find_element(By.ID, id_input_username).send_keys(username)
    driver.find_element(By.ID, id_input_personalid).send_keys(personalid)
    driver.find_element(By.ID, id_input_password).send_keys(password)

    driver.find_element(By.ID, id_login).click()

    try:
        elem = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.ID, id_courses))
        )
    except TimeoutException:
        print("Timeout!")
        driver.quit()

    print("Logged into moodle")
    return driver


def driver_goto_moodle_main(driver: webdriver.Chrome):

    driver.get(url_moodle_mainscreen)
    try:
        elem = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.ID, id_courses))
        )
    except TimeoutException:
        print("Timeout!")
        driver.quit()


    # Assuming sidebar is alive
def driver_get_courses(driver: webdriver.Chrome):
    print("Getting courses")
    sidebar = driver.find_element(By.ID,id_courses)
    sidebar_html_str = sidebar.get_attribute("innerHTML")
    res = moodleXpath.xpath_get_courses(sidebar_html_str)

    return res


def driver_crawl_course(driver: webdriver.Chrome, url: str):
    driver.get(url)
    coursecontent = driver.find_element(By.CLASS_NAME,value="course-content")
    course_html = coursecontent.get_attribute("innerHTML")
    resources = moodleXpath.xpath_get_course_resources(course_html)
    return resources


def driver_crawl_assignment(driver: webdriver.Chrome, url: str):
     driver.get(url)
     try:
         elem = WebDriverWait(driver, TIMEOUT).until(
             EC.presence_of_element_located((By.ID, id_assignment_box)))
     except TimeoutException:
         print("Timeout!")
         driver.quit()

     html_str = driver.page_source
     name, deadline, files_names, files_links = moodleXpath.xpath_get_assignment(html_str)

     for link in files_links:
         driver.get(link)

     return (name,deadline,files_names)



def main():
    dirname = os.path.dirname(__file__)
    fullpath = os.path.join(dirname, 'Downloaded')
    username="alonharell"
    personalid="318509403"
    password="TauWelcome27"
    print(fullpath)
    assignments = []
    driver = driver_init_login(username=username, personalid=personalid, password=password,path=fullpath)
    courses = driver_get_courses(driver)
    course_filter = lambda cid: cid.startswith("368")
    for course in courses:
        course_id, course_name, course_link = course
        if (course_filter(course_id)):
            resources = driver_crawl_course(driver, course[2])
            for resource in resources:
                resource_name, resrouce_type, resource_id, resource_link = resource
                if ("assign" in resrouce_type):
                    #assignment_name, assignment_deadline, files_names, files_links = driver_crawl_assignment(driver,resource_link)
                    assignment_name,deadline,files_names = driver_crawl_assignment(driver,resource_link)
                    assignments.append((username,course_name,course_id,resource_link,assignment_name,deadline,files_names))


    for assignment in assignments:
        username, course_name, course_id, resource_link, assignment_name, deadline, files_names = assignment
        print((username, course_name, course_id, resource_link, assignment_name, deadline, files_names))
        moodleGetFrom.write_moodle_file(username, course_name, course_id, resource_link, assignment_name, deadline, files_names)



    driver.quit()

if __name__ == "__main__":
    main()