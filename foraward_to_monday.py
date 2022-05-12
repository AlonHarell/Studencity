import monday
from monday import MondayClient
import json

import requests
from moodleGetFrom import get_course_list, get_course_resources, get_resource_assignment

from APIKey import apiKey
monday = MondayClient(apiKey)

#our_board = 2663355974

# returns list of (resource_name, resource_type, resource_link)


def get_board_id_by_name(board_name):
    boards = monday.boards.fetch_boards()['data']['boards']
    for b in boards:
        if(b['name'] == board_name):
            return b['id']
    return None


def get_group_id_by_title(board_id, group_title):
    groups = monday.groups.get_groups_by_board(
        [board_id])['data']['boards'][0]['groups']
    for g in groups:
        if g['title'] == group_title:
            return g['id']
    return None


def get_column_id_by_board_id_and_title(board_id, col_title):
    board = monday.boards.fetch_boards_by_id(board_id)['data']['boards'][0]
    cols = board['columns']
    for col in cols:
        if col['title'] == col_title:
            return col['id']
    return None


def get_item_id_by_name(board_id, group_id, item_name):
    items = monday.groups.get_items_by_group(
        board_id, group_id)['data']['boards'][0]['groups'][0]['items']
    for item in items:
        if item['name'] == item_name:
            return item['id']
    return None


#print(get_column_id_by_board_id_and_title(2666621719, 'Submission Date'))
# print(monday.boards.fetch_boards())
# print(monday.boards.fetch_boards_by_id())
# print(get_item_id_by_name(2663355974, get_group_id_by_title(
#     2663355974, 'Course Excercises'), "Excercise 1"))

# id = get_item_id_by_name(2663355974, get_group_id_by_title(
#     2663355974, 'Course Excercises'), "Excercise 1")
# print(id)
# print(monday.items.fetch_items_by_id([id]))


def add_assignment_to_monday(board_id, assignments_list, assignment_name, group_assignment_id):
    for a in assignments_list:
        username = a[0]
        a_course = a[1]
        a_url = a[3]
        a_name = a[4]
        a_submit_date = a[5]
        a_path_list = a[6]
        monday.items.create_item(
            board_id, group_assignment_id, assignment_name)
        a_id = get_item_id_by_name(
            board_id, group_assignment_id, assignment_name)
    #monday.items.change_item_value(board, a_id, )
    #print(monday.groups.get_items_by_group(our_board, 'matalot5384'))


def add_item_to_group(boardID, groupID, item):
    monday.items.create_item(board_id=str(
        boardID), group_id=groupID,  item_name=item)


def delete_group(boardID, groupID):
    monday.groups.delete_group(boardID, groupID)


def change_col_val(itemID, boardID, colID, val):

    query = f"mutation {{change_simple_column_value(item_id: {itemID}, board_id: {boardID}, column_id: \"{colID}\", value: \"{val}\") {{    id  }}}}"
    apiUrl = "https://api.monday.com/v2"
    headers = {"Authorization": apiKey}
    data = {'query': query}
    r = requests.post(url=apiUrl, json=data, headers=headers)


def get_account_id(board_id):
    data = monday.boards.fetch_boards_by_id([board_id])
    return 30386827
    return data["account_id"]


def add_person_to_task(itemID, boardID, colID):
    person = f"{{\"id\": {get_account_id(boardID)}}}"
    change_col_val(itemID, boardID, colID, person)


change_col_val(2666502272, 2663355974, "date4", "2019-06-03 13:25:00")

add_person_to_task(2666502272, 2663355974, "person")
