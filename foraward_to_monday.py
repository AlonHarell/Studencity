import monday
from monday import MondayClient
import json
from moodleGetFrom import get_course_list, get_course_resources, get_resource_assignment


apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE2MDE2NjY2OSwidWlkIjozMDM4NjgyOSwiaWFkIjoiMjAyMi0wNS0xMlQwNzo1MzozNi4zNzBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTE4NzU5MjIsInJnbiI6InVzZTEifQ.lGl7qoVNCeKwzXloL2LF57elitPglyddpzyrTVC_Gx4"

monday = MondayClient(apiKey)

our_board = 2663355974

# returns list of (resource_name, resource_type, resource_link)


def get_groups_ids_by_name():
    groups = monday.groups.get_groups_by_board(
        [our_board])['data']['boards'][0]['groups']
    gruops_ids = []
    for i in range(len(groups)):
        id = groups[i]['id']
        gruops_ids.append(id)


def get_assignments(group_assignment_id):
    resources = get_course_resources()
    assignments = [(x[0], x[2]) for x in resources if x[1] == 1]
    assignments_info = dict()
    for a in assignments:
        assignments_info[a[0]] = get_resource_assignment(a[1])
        monday.items.create_item(our_board, group_assignment_id, a[0])
    #print(monday.groups.get_items_by_group(our_board, 'matalot5384'))
