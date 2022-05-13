import monday
from monday import MondayClient
import json

import requests

from APIKey import apiKey
monday = MondayClient(apiKey)


GROUP_NAME = 'Course Excercises'
#our_board = 2663355974

# returns list of (resource_name, resource_type, resource_link)


def get_board_id_by_name(board_name):
    print(monday.boards.fetch_boards())
    boards = monday.boards.fetch_boards()['data']['boards']
    print(boards)
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
    print(r)


def get_account_id(board_id):
    data = monday.boards.fetch_boards_by_id([board_id])
    return 30386827
    return data["account_id"]


def add_person_to_task(itemID, boardID, colID):
    person = f"{{\"id\": {get_account_id(boardID)}}}"
    change_col_val(itemID, boardID, colID, person)


def create_link_json(url, text):
    return f"{{\"url\":\"{url}\",\"text\":\"{text}\"}}"


link = create_link_json("http://monday.com", "Go to Monday!")
#print(get_column_id_by_board_id_and_title(2666621719, 'Submission Date'))
# print(monday.boards.fetch_boards())
# print(monday.boards.fetch_boards_by_id())
# print(get_item_id_by_name(2663355974, get_group_id_by_title(
#     2663355974, 'Course Excercises'), "Excercise 1"))

# id = get_item_id_by_name(2663355974, get_group_id_by_title(
#     2663355974, 'Course Excercises'), "Excercise 1")
# print(id)
# print(monday.items.fetch_items_by_id([id]))


def add_assignments_to_monday(assignments_list):
    for a in assignments_list:
        username = a[0]
        a_course = a[1]
        a_course_id = a[2]
        a_url = a[3]
        a_name = a[4]
        a_submit_date = a[5]
        a_path_list = a[6]
        a_board_id = 2666624447  # get_board_id_by_name(a_course_id)
        a_group_id = get_group_id_by_title(a_board_id, GROUP_NAME)
        # adding new assignment item to course board
        monday.items.create_item(
            a_board_id, a_group_id, a_name)
        a_id = get_item_id_by_name(
            a_board_id, a_group_id, a_name)
        print(a_id)
        # add submission date
        submit_date_col_id = get_column_id_by_board_id_and_title(
            a_board_id, 'Submission Date')
        print(a_submit_date)
        print(submit_date_col_id)
        change_col_val(a_id, a_board_id, submit_date_col_id, a_submit_date)
        # add files
        # files_col_id = get_column_id_by_board_id_and_title(
        #     a_board_id, 'Files')
        # for f in a_path_list:
        #     monday.items.add_file_to_column(a_id, files_col_id, f)
        # add submission
        submission_col_id = get_column_id_by_board_id_and_title(
            a_board_id, 'Submission')
        change_col_val(a_id, a_group_id, submission_col_id, a_url)


# Test for נושאים ב
 # adding new assignment item to course board
# a_board_id = 2666626328
# a_group_id = get_group_id_by_title(a_board_id, GROUP_NAME)
# a_name = 'aadsds'
# a_submit_date = '2000-12-04'
# monday.items.create_item(
#     a_board_id, a_group_id, a_name)
# a_id = get_item_id_by_name(
#     a_board_id, a_group_id, a_name)
# # add submission date
# submit_date_col_id = get_column_id_by_board_id_and_title(
#     a_board_id, 'Submission Date')
# change_col_val(a_id, a_board_id, submit_date_col_id, a_submit_date)
# # add files
# # files_col_id = get_column_id_by_board_id_and_title(
# #     a_board_id, 'Files')
# # for f in a_path_list:
# #     monday.items.add_file_to_column(a_id, files_col_id, f)
# # add submission
# submission_col_id = get_column_id_by_board_id_and_title(
#     a_board_id, 'Submission')
# print(change_col_val(a_id, a_group_id, submission_col_id, link))

# group_id = get_group_id_by_title(2666626328, 'Course Excercises')
# item_id = get_item_id_by_name(2666626328, group_id, 'EX222')
# files_col_id = get_column_id_by_board_id_and_title(
#     2666626328, 'Files')
# monday.items.add_file_to_column(item_id, files_col_id)

#print(get_column_id_by_board_id_and_title(2666626328, 'Submission Date'))
#monday.items.add_file_to_column(2666626692, files_col_id, f)
#monday.items.change_item_value(board, a_id, )
#print(monday.groups.get_items_by_group(our_board, 'matalot5384'))


# change_col_val(2666502272, 2663355974, "date4", "2019-06-03 13:25:00")

# add_person_to_task(2666502272, 2663355974, "person")
