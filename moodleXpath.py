import lxml.html

def str_to_content(html_str:str):
    return lxml.html.fromstring(html_str)

def xpath_get_courses(html_str:str):
    query_courses = "//li[.//div/@class='ml-1']//text()"
    content = str_to_content(html_str)
    print("Running xpath")
    return content.xpath(query_courses)