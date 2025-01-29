from student import Student

if __name__ == "__main__":

    x = int(input("How many objects of Student class do you want to make: "))
    lst_students = []

    for i in range(1, x+1):
        name = input(f"Enter the name of student #{i}: ")
        surname = input(f"Enter the surname of student #{i}: ")
        student_id = int(input(f"Enter the student ID #{i}: "))
        major = input(f"Enter the major of student #{i}: ")
        gpa = float(input(f"Enter the gpa of student #{i}: "))

        lst_students.append(Student(name, surname, student_id, major, gpa))

    for person in lst_students:
        person.display_info()
        print(f"The Grade is {person.get_alphabetic_grade()}")

