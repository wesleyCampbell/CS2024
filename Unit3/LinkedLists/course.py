"""
Provides the Course ADT.
"""


class Course:
    """
    A node in the courselist linked list ADT.
    Structured for a class with a number, name, grade, ect.
    Points to the next node in the list.
    """

    def __init__(self, num=0, name="", hours=0.0, gpa=0.0):
        """
        Constructor for the Course node class.

        Paramaters:
        -----------
        num : String
            The course number
        name : String
            The course name
        hours : Float
            The credit hours of the course
        gpa : Float
            The grade point average of the course

        Returns:
        --------
        None
        """
        if type(num) != int or num < 0:
            raise(ValueError("Num must be positive integer"))
        self._number = num

        if type(name) != str:
            raise(ValueError("Name must be String"))
        self._name = str(name)

        if type(hours) != float or hours < 0:
            raise(ValueError("Hours must be positive float"))
        self._credit_hours = hours

        if type(gpa) != float or gpa < 0:
            raise(ValueError("GPA must be positive float"))
        self._grade = gpa

        self.next = None

    def number(self):
        """
        Standard getter for course number
        """
        return self._number

    def name(self):
        """
        Standard getter for course name
        """
        return self._name

    def credit_hr(self):
        """
        Standard getter for course hours
        """
        return self._credit_hours

    def grade(self):
        """
        Standard getter for course grade
        """
        return self._grade

    def set_next(self, course):
        """
        Standard getter for next pointer
        """
        self.next = course

    def __str__(self):
        """
        Overrides the builtin string function.
        """
        return f"{self.number()} {self.name()} Grade:{self.grade()} Hours {self.credit_hr()}"
