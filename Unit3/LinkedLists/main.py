"""
Main driver file for the Linked Lists module
"""

import os
from course import Course
from courselist import CourseList

DATAPATH = "Unit3/LinkedLists/data.txt"


def get_data(filepath):
    """
    Collects data from a datafile
    """
    working_directory = os.getcwd()

    course_list = CourseList()
    with open(os.path.join(working_directory, filepath), "r") as data:
        for line in data.readlines():
            values = line.strip().split(',')

            values[0], values[2], values[3] = int(
                values[0]), float(values[2]), float(values[3])

            course_list.insert(Course(*values))

    return course_list


def main():
    """
    The main function for main.py
    """
    course_list = get_data(DATAPATH)
    print(course_list)


if __name__ == "__main__":
    main()
