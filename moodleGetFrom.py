
# returns list of (course_id, course_name)
def get_course_list() -> list[(int, str)]:
    return []


# returns list of (resource_name, resource_type, resource_link, resource_course)
def get_course_resources() -> list[(str, int, str, str)]:
    # RESTYPE_ASSIGNMENT = 1
    # RESTYPE_FORUM = 2
    # RESTYPE_DOCUMENT = 3

    return []


def get_resource_assignment(resource_link) -> dict:
    # given assignment link, return dict of assignment info: sumbission date, Files
    return dict()
