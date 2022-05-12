import monday
from monday import MondayClient
import json
from moodleGetFrom import get_course_list, get_course_resources, get_resource_assignment
from APIKey import apiKey

monday = MondayClient(apiKey)

#our_board = 2663355974

# returns list of (resource_name, resource_type, resource_link)


def get_group_id_by_title(board, group_title):
    groups = monday.groups.get_groups_by_board(
        [board])['data']['boards'][0]['groups']
    for g in groups:
        if g['title'] == group_title:
            return g['id']
    return None


def get_item_id_by_name(board, group_id, item_name):
    items = monday.groups.get_items_by_group(
        board, group_id)['data']['boards'][0]['groups'][0]['items']
    for item in items:
        if item['name'] == item_name:
            return item['id']
    return None


# print(get_item_id_by_name(2663355974, get_group_id_by_title(
#     2663355974, 'Course Excersizes'), "Excersize 1"))

# id = get_item_id_by_name(2663355974, get_group_id_by_title(
#     2663355974, 'Course Excersizes'), "Excersize 1")
# print(monday.items.fetch_items_by_id(2663355974, [id]))


def get_assignments(board, group_title):
    #group_assignment_id = get_group_id_by_title(board, group_title)
    resources = get_course_resources()
    assignments = [(x[0], x[2], x[3]) for x in resources if x[1] == 1]
    #assignment = (assignment_name, assignment_link, assignment_course)
    assignments_info = dict()
    for a in assignments:
        a_name = a[0]
        a_link = a[1]
        assignments_info[a_name] = get_resource_assignment(a_link)
    return assignments_info


def add_assignment_to_monday(board, assignments_info, assignment_name, group_assignment_id):
    a_submit_date = assignments_info[assignment_name]['Submission Date']
    a_files = assignments_info[assignment_name]['Files']
    monday.items.create_item(board, group_assignment_id, assignment_name)
    a_id = get_item_id_by_name(board, group_assignment_id, assignment_name)
    #monday.items.change_item_value(board, a_id, )
    #print(monday.groups.get_items_by_group(our_board, 'matalot5384'))


group_assignment_id = get_group_id_by_title(2663355974, 'Course Excercises')
monday.items.create_item(str(2663355974), group_assignment_id, 'EX222')
