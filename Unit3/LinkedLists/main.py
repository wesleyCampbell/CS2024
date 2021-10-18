"""
Main driver file for the Linked Lists module
"""

import random
from course import Course
from courselist import CourseList


def main():
    """
    The main function for main.py
    """
    courselist = CourseList()

    for _ in range(10):
        value = random.randint(0, 1000)
        courselist.insert(Course(value))

    for course in courselist:
        print(course)


if __name__ == "__main__":
    main()
