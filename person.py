class Person:
    def __init__(self, name, surname, student_id=None, major=None, gpa=None):
        self.name = name
        self.surname = surname
        self.student_id = student_id
        self.major = major
        self.gpa = gpa

    def get_major(self):
        print(f"{self.name} {self.surname} has major in {self.major}")

    def walk(self):
        print(f"{self.name} {self.surname} is walking")

    def get_info(self):
        print(f"The student {self.name} {self.surname}, id: {self.student_id} and gpa: {self.gpa}")

