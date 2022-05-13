import json
from os.path import exists

#filename would be: username_moodle.something
#if file alredy exists, update the assignemnt in it

def write_moodle_file(username:str, course_name:str, course_id:str, assignmet_url:str, assignment_name:str, assignment_deadline:str, paths:list):
    user_filename = username + "_moodle.json"
    file_exists = False
    if exists(user_filename):
        file_exists = True

    dict_assignment = {
        "assignment_name": assignment_name,
        "assignmet_url": assignmet_url,
        "assignment_deadline": assignment_deadline,
        "paths": paths
    }

    dict_course = {
        "course_name": course_name,
        "course_id": course_id,
        "assignments": [dict_assignment]
    }

    user_moodle = {
        "username": username,
        "courses": [dict_course]
    }

    if not file_exists:
        with open(user_filename, "a+") as user_file:
            json.dump(user_moodle, user_file)
            return None

    #if file alredy exists
    with open(user_filename, "r+",encoding="utf-8",errors='ignore') as user_file:
        data = json.load(user_file,strict=False)
        courses_lst = data["courses"]
        course_exists = False
        course_found = None
        for c in courses_lst:  #check if this course is already in the list
            if course_name in c.values():
                course_exists = True
                course_found = c
                break
        if course_exists:
            course_found["assignments"].append(dict_assignment)
        else:
            courses_lst.append(dict_course)
        user_file.seek(0,0)
        json.dump(data,user_file)



def read_moodle_file(filepath):
    json.load(filepath)

    #for each assignment in file:
    #(username, course_name, course_id, assignemt_url, assignment_name, assignment_deadline, [paths of resources of assignment])




#print (write_moodle_file(username="balulu",course_name="new course 2",course_id="maroon6", assignmet_url="ricky this is my business", assignment_name="ze meatzben oti", assignment_deadline="mahar", paths=['TAU']))

# with open("./hi", "w") as thefile:
#   json.dump("{\"sup\": 2}", thefile) 

# with open("./hi", "r") as thefile:
#   a = json.load(thefile)

# print(a) 