from person import Person

if __name__ == "__main__":

    person1 = Person('Ruslan', 'Asanov', student_id=1)
    person2 = Person('Aman', 'Talgatov', student_id=1)
    person3 = Person('Sultan', 'Bakytbek uulu', student_id=1)
    person4 = Person('Damir', 'Imanaliev', student_id=1)

    lst = [person1, person2, person3, person4]


    for x in lst:
        print(x.walk())

