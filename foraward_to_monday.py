import monday
from monday import MondayClient
import json

import requests
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


def add_item_to_group(boardID, groupID, item):
        monday.items.create_item(board_id=str(boardID), group_id=groupID,  item_name=item)


def delete_group(boardID, groupID):
        monday.groups.delete_group(boardID, groupID)

    
def change_col_val(itemID, boardID, colID, val):

        query = f"mutation {{change_simple_column_value(item_id: {itemID}, board_id: {boardID}, column_id: \"{colID}\", value: \"{val}\") {{    id  }}}}"
        apiUrl = "https://api.monday.com/v2"
        headers = {"Authorization" : apiKey}
        data = {'query' : query}
        r = requests.post(url=apiUrl, json=data, headers=headers)

def get_account_id(board_id):
    data = monday.boards.fetch_boards_by_id([board_id])
    return 30386827
    return data["account_id"]

def add_person_to_task(itemID, boardID, colID):
    person =  f"{{\"id\": {get_account_id(boardID)}}}"
    change_col_val(itemID, boardID, colID, person)

change_col_val(2666502272,2663355974,"date4","2019-06-03 13:25:00")

add_person_to_task(2666502272,2663355974,"person")