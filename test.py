import requests
import json
#import "queries.gql"

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE2MDE2NjI2MCwidWlkIjozMDM4NjgyNywiaWFkIjoiMjAyMi0wNS0xMlQwNzo1MToxOS45MDhaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTE4NzU5MjIsInJnbiI6InVzZTEifQ.SHDse5A2xm7LAD3geFPK7VD0e8GW2jf42tU-LDJutYU"


from monday import MondayClient
our_board = 2663355974

monday = MondayClient(apiKey)



# monday.items.create_item(board_id=our_board, group_id='today',  item_name='ricky this is my business')
#monday.items.create_item(our_board, 'Courses', "ricky this is my business")
#print(monday.boards.fetch_boards())
#monday.boards.
#print(monday.boards.fetch_boards_by_id([our_board]))

# print(monday.groups.get_groups_by_board([2663355974]))

# monday.items.fetch_items_by_id(our_board, [])
# print(monday.items.fetch_items_by_id(our_board, [2663356011]))

# print(monday.boards.fetch_boards_by_id(our_board))

data = monday.groups.get_groups_by_board([our_board])
#monday.items.create_item(board_id=str(our_board), group_id='topics',  item_name='ricky this is my business')
#monday.groups.create_group(our_board, "matalot")
print (data)

print(dir(monday.boards.__dict__.keys())