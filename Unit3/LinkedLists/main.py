from course import Course
from courselist import CourseList
import random


def main():
    courselist = CourseList()

    for i in range(2):
        courselist.insert(Course(i+1))

    print(courselist)


if __name__ == "__main__":
    main()
