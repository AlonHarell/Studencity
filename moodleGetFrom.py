import json
from os.path import exists

#filename would be: username_moodle.something
#if file alredy exists, update the assignemnt in it

def write_moodle_file(username:str, course_name:str, course_id:str, assignmet_url:str, assignment_name:str, assignment_deadline:str, paths:list):
    user_filename = username + "_moodle.json"
    file_exists = False
    if exists(user_filename):
      file_exists = True
    # if not file_exists:
    user_moodle = {
      "username": username,
      "courses": [
        {
          "course_name": course_name, 
          "course_id": course_id, 
          "assignments": [
            {
              "assignment_name": assignment_name, 
              "assignmet_url": assignmet_url,
              "assignment_deadline": assignment_deadline,
              "paths": paths
            }
          ]
        }
      ]
    }
    if not file_exists:
      with open(user_filename, "a+") as user_file:
          json.dump(user_moodle, user_file)
          return None
    with open(user_filename, "a+") as user_file:
      data = json.load(user_file)
      courses = data["courses"]
      course_exists = False
      course_found = None
      for c in courses:
        if course_name in c.values():
          course_exists = True
          course_found = c
          break
        #if flag is down, then add new course
      if not course_exists:  #check if this course is already in the list
        course_dict = {
            "course_name": course_name, 
            "course_id": course_id, 
            "assignments": [
              {
                "assignment_name": assignment_name, 
                "assignmet_url": assignmet_url,
                "assignment_deadline": assignment_deadline,
                "paths": paths
              }
            ]
          }
        courses.append(course_dict)
        json.dump(user_moodle, user_file)
        return None
      else: #the course IS there
        new_assignment = {
                          "assignment_name": assignment_name, 
                          "assignmet_url": assignmet_url,
                          "assignment_deadline": assignment_deadline,
                          "paths": paths
                        }
        course_found["assignments"].append(new_assignment)
      return None


def read_moodle_file(filepath):

  with open(filepath, 'r') as file:
    ret_val = []
    jsonfile = json.load(file)
    username = jsonfile['username']
    for course in jsonfile["courses"]:
      for key, val in course.items():
        if key=="assignments":
          for asign in val:
            ret_val.append((username, course['course_name'], course['course_id'], asign['assignmet_url'], asign['assignment_name'], asign['assignment_deadline'],asign['paths']))

  return ret_val



# print (write_moodle_file(username="balulu",course_name="new course 1",course_id="maroon6", assignmet_url="ricky this is my business", assignment_name="ze meatzben oti", assignment_deadline="mahar", paths=['TAU']))
# print(read_moodle_file("./balulu_moodle.json"))
# with open("./hi", "w") as thefile:
#   json.dump("{\"sup\": 2}", thefile) 

# with open("./hi", "r") as thefile:
#   a = json.load(thefile)

# print(a) 