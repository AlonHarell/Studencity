from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

import moodleXpath

import time

url_moodle = "https://moodle.tau.ac.il/"
url_moodle_mainscreen = "https://moodle.tau.ac.il/my/"
id_connect_to_moodle = "clicktoconnect"
id_input_username = "Ecom_User_ID"
id_input_personalid = "Ecom_User_Pid"
id_input_password = "Ecom_Password"
id_login = "loginButton2"
id_courses = "nav-drawer"
TIMEOUT = 30


def driver_init_login(username, personalid, password) -> webdriver.Chrome:
    #### ids


    ### options
    driver_options = options.Options()
    driver_options.headless = True
    service = Service(ChromeDriverManager().install())

    ### init driver
    driver = webdriver.Chrome(service=service, options=driver_options)

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
    print(res)

    return res


def driver_course_crawl(driver: webdriver.Chrome, url: str):
    driver.get()


def main():
    driver = driver_init_login(username="alonharell", personalid="318509403", password="TauWelcome27")
    courses = driver_get_courses(driver)
    course_filter = lambda course_id: course_id.startswith("368")
    for course in courses:
        if (course_filter):
            pass

    driver.quit()

if __name__ == "__main__":
    main()