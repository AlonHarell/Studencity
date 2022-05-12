import lxml.html

def str_to_content(html_str:str):
    return lxml.html.fromstring(html_str)

def xpath_get_courses(html_str:str):
    query_courses_ids = "//li[.//div/@class='ml-1']/a/@data-key"
    query_courses_names = "//li[.//div/@class='ml-1']//text()"
    query_courses_links = "//li[.//div/@class='ml-1']/a/@href"
    content = str_to_content(html_str)
    print("Running xpath: courses")
    res_names = content.xpath(query_courses_names)
    res_links = content.xpath(query_courses_links)
    res_ids = content.xpath(query_courses_ids)
    counter = 0
    courses = []
    for course_name in res_names:
        if (not course_name.startswith("\n")):
            courses.append((res_ids[counter],course_name,res_links[counter]))
            counter += 1

    return courses


#currently filtered to only return assignments!!!!!!!
def xpath_get_course_resources(html_str:str):
    print("Running xpath: resources")
    RESTYPE_ASSIGNMENT = 1
    RESTYPE_FORUM = 2
    RESTYPE_DOCUMENT = 3
    query_get_resources = "//li[starts-with(./@class,'activity')]"
    query_resource_get_names = f"{query_get_resources}//span[@class = 'instancename']/text()"
    query_resource_get_types = f"{query_get_resources}/@class"
    query_resource_get_ids = f"{query_get_resources}/@id"
    query_resource_get_links = f"{query_get_resources}//a[./@class = 'aalink']/@href"

    content = str_to_content(html_str)
    results_names = content.xpath(query_resource_get_names)
    results_types = content.xpath(query_resource_get_types)
    results_ids = content.xpath(query_resource_get_ids)
    results_links = content.xpath(query_resource_get_links)

    resources = []

    if not(len(results_links) == len(results_ids) == len(results_types) == len(results_names)):
        print("Warning: different lengths")

    for i in range(0,len(results_names)):
        resource = (results_names[i],results_types[i],results_ids[i],results_links[i])
        resources.append(resource)


    return resources


def xpath_get_assignment(html_str:str):
    print("Running xpath: assignment")
    boxname = "box py-3 boxaligncenter submissionsummarytable py-3"
    get_main = "//div[./@role = 'main']"
    query_get_name = f"{get_main}/h2/text()"
    get_box = f"{get_main}//div[@class = '{boxname}']"
    query_get_deadline = f"{get_box}/table/tbody/tr[4]/td/text()"
    query_get_files_names = f"//div[@id = 'intro']//div[@class = 'fileuploadsubmission']/a/text()"
    query_get_files_links = f"//div[@id = 'intro']//div[@class = 'fileuploadsubmission']/a/@href"

    content = str_to_content(html_str)
    name=None
    deadline=None
    try:
        name = content.xpath(query_get_name)[0]
        deadline = content.xpath(query_get_deadline)[0]
    except IndexError:
        print("WARNING: IndexError")

    files_names = content.xpath(query_get_files_names)
    files_links = content.xpath(query_get_files_links)
    #TODO: remove my submissions
    #TODO:

    return (name,deadline,files_names,files_links)