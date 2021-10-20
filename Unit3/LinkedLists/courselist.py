"""
Provides the CourseList ADT.
"""


class CourseList:
    """
    A Linked list where each node is a Course
    """

    def __init__(self):
        """
        Constructor for the CourseList class.
        It functions as a linked list of Courses.
        """
        self.head = None
        self._size = 0

    def insert(self, course):
        """
        Inserts a value onto the top of the linked list.

        Paramaters:
        -----------
        course : Course
            The course to add to the list

        Returns:
        --------
        None
        """
        course_num = course.number()
        current_course = self.head
        is_head = True

        if current_course is None:
            self.head = course

        else:
            while current_course.next is not None and course_num >= current_course.next.number():
                current_course = current_course.next
                is_head = False

            # If the current_course is not the head of the list
            if not is_head:
                course.set_next(current_course.next)
                current_course.set_next(course)
            # If the current course is the head of the list
            else:
                if course_num > current_course.number():
                    course.set_next(self.head.next)
                    self.head.set_next(course)
                else:
                    course.set_next(self.head)
                    self.head = course

        self._size += 1

    def remove(self, number):
        """
        Removes a course with the given course number.

        Paramaters:
        -----------
        number : Int
            The course number of the course to be removed

        Returns:
        --------
        None
        """
        previous_course = None
        current_course = self.head

        # Traverse through each value until the course numbers match
        while current_course.number() <= number and current_course.next is not None:
            previous_course = current_course
            current_course = current_course.next

        # If the course is not the first course in the list
        if current_course.number() == number and previous_course is not None:
            previous_course.set_next(current_course.next)

        # If the course is the first course in the list
        elif current_course.number() == number and previous_course is None:
            self.head = current_course.next

        self._size -= 1
        del current_course

    def remove_all(self, number):
        """
        Removes all occurances of the course with given course number.

        Paramaters:
        -----------
        number : Int
            The course number of the courses to be removed

        Returns:
        --------
        None
        """
        previous_course = None
        current_course = self.head

        # Traverse through each item in the list
        while current_course.next is not None:
            # If the course numbers match and the value is not the first one
            if current_course.number() == number and previous_course is not None:
                previous_course.set_next(current_course.next)
                self._size -= 1
            # IF the course numbers match and the value is the first one
            elif current_course.number() == number and previous_course is None:
                self.head = current_course.next
                self._size -= 1
            # If the course numbers do not match up
            else:
                previous_course = current_course

            # Go to the next value
            current_course = current_course.next

        # If the last value matches the target
        if current_course.number() == number:
            previous_course.set_next(None)

    def find(self, number):
        """
        Finds the first course with the course number provided.

        Paramaters:
        -----------
        number : Int
            The course number of the course to be found

        Returns:
        --------
        (int):
            The index of the course found, or - 1 if not found.
        """
        counter = 0
        current_course = self.head

        # Traverse through each value in the list until course numbers match
        while current_course.next is not None:
            # If the course numbers match
            if current_course.number() == number:
                return current_course

            # Increment
            current_course = current_course.next
            counter += 1

        return None if current_course.number() != number else current_course

    def size(self):
        """
        Returns how many courses are in the list
        """
        return self._size

    def calculate_gpa(self):
        """
        Calculates the cumulative gpa of the list

        Returns:
        --------
        (Float): The cummulative gpa
        """
        gpa_sum = 0
        hr_sum = 0

        course = self.head

        if course is None:
            return 0.0

        while course.next is not None:
            gpa_sum += course.grade() * course.credit_hr()
            hr_sum += course.credit_hr()

            course = course.next

        gpa_sum += course.grade() * course.credit_hr()
        hr_sum += course.credit_hr()

        return gpa_sum / hr_sum

    def is_sorted(self):
        """
        Checks wheter the linked list is in acending order.

        Returns:
        --------
        (Boolean): Is the list sorted?
        """
        # Traverse the list
        previous = self.head

        if previous is None:
            return True

        current = self.head.next

        while current.next is not None:
            if current.number() < previous.number():
                return False

            previous = current
            current = current.next

        return current.number() > previous.number()

    def __str__(self) -> str:
        # Traverse each course and add it to string
        current_course = self.head
        output = ""
        while current_course.next is not None:
            output += str(current_course) + '\n'
            current_course = current_course.next

        return output + str(current_course) + '\n'

    def __iter__(self):
        """
        Returns an iterative helper class; initializes iteration

        Returns:
        --------
        (_CourseListIterativeHelper) : An iterative helper!
        """
        return _CourseListIterativeHelper(self)


class _CourseListIterativeHelper:
    def __init__(self, courselist: CourseList):
        self._head = courselist.head

        self._current_course = None
        self._next_course = self._head

    def __iter__(self) -> object:
        """
        Initializes an iteration

        Returns:
        --------
        (_CourseListIterativeHelper) : self
        """
        self._current_course = None
        self._next_course = self._head

        return self

    def __next__(self) -> int:
        """
        Returns the next course in an iteration.

        Returns:
        --------
        (Int) : The Course number
        """
        if self._next_course is None:
            raise StopIteration

        self._current_course = self._next_course
        self._next_course = self._next_course.next

        return self._current_course.number()
