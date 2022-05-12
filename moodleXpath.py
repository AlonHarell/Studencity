import lxml.html

def str_to_content(html_str:str):
    return lxml.html.fromstring(html_str)

def xpath_get_courses(html_str:str):
    query_courses_ids = "//li[.//div/@class='ml-1']/a/@data-key"
    query_courses_names = "//li[.//div/@class='ml-1']//text()"
    query_courses_links = "//li[.//div/@class='ml-1']/a/@href"
    content = str_to_content(html_str)
    print("Running xpath")
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



