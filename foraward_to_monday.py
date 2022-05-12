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


def get_item_id_by_title(board, group_id, item_title):
    items = monday.groups.get_items_by_group(board, group_id)


def get_assignments(board, group_title):
    group_assignment_id = get_group_id_by_title(board, group_title)
    resources = get_course_resources()
    assignments = [(x[0], x[2]) for x in resources if x[1] == 1]
    assignments_info = dict()
    for a in assignments:
        a_name = a[0]
        a_link = a[1]
        assignments_info[a_name] = get_resource_assignment(a_link)
        a_submit_date = assignments_info[a_name]['submition_date']
        monday.items.create_item(board, group_assignment_id, a_name)
        monday.items.change_item_value(board, a_name, )
    #print(monday.groups.get_items_by_group(our_board, 'matalot5384'))
