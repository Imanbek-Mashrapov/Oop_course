class Student:
    def __init__(self, name=None, surname=None, studentID=None, major=None, gpa=None):
        self.name = name
        self.surname = surname
        self.studentID = studentID
        self.major = major
        self.gpa = gpa

    def display_info(self):
        print(f"The student is {self.name} {self.surname}, id: {self.studentID}, major: {self.major}, gpa: {self.gpa}")

    def get_alphabetic_grade(self):
        if self.gpa is None:
            return None

        if self.gpa >= 85:
            return 'A'
        elif self.gpa >= 70:
            return 'B'
        elif self.gpa >= 60:
            return 'C'
        elif self.gpa >= 50:
            return 'D'
        else:
            return 'F'

