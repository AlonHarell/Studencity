from monday import MondayClient
import requests
import json

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE2MDE2NjY2OSwidWlkIjozMDM4NjgyOSwiaWFkIjoiMjAyMi0wNS0xMlQwNzo1MzozNi4zNzBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTE4NzU5MjIsInJnbiI6InVzZTEifQ.lGl7qoVNCeKwzXloL2LF57elitPglyddpzyrTVC_Gx4"

our_board = 2663355974
monday = MondayClient(apiKey)


# print(monday.boards.fetch_items_by_board_id([our_board]))
# print(monday.groups.get_groups_by_board(our_board))
g = monday.groups.get_groups_by_board(
    [our_board])['data']['boards'][0]['groups']
g_ids = []
for i in range(len(g)):
    id = g[i]['title']
    g_ids.append(id)
print(g_ids)
