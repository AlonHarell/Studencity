import moodleExtraction
import moodleGetFrom
from foraward_to_monday import add_assignments_to_monday
import sys


def main(username, pid, password):
    moodleExtraction.main(username, pid, password)
    filepath = username+"_moodle.json"
    assignments_list = moodleGetFrom.read_moodle_file(filepath)
    add_assignments_to_monday(assignments_list)


if __name__ == "__main__":
    args = sys.argv
    username = args[1]
    pid = args[2]
    password = args[3]
    main(username, pid, password)

