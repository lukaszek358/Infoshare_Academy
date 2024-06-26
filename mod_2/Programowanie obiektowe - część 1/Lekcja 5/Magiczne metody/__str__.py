# METODA print() ZWRACA NAM PRZYWOŁANĄ W NIEJ WARTOŚĆ POD POSTACIĄ TEKSTOWĄ (str) - INACZEJ MÓWIĄC KONWERTUJE JĄ NA WARTOŚĆ STRING
# METDOA __str__ JEST TOŻSAMA Z METODĄ print()  - KONWERTUJE NAM PRZYWOŁANĄ WARTOŚĆ NA CIĄG TEKSTOWY
# METODA _str__ ZWRACA NAM NIEFORMALNĄ REPREZENTACJĘ NASZEGO OBIEKTU (W ZWIĘZŁEJ DO WYPISANIA FORMIE)

import random
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}, Promoted: {self.promoted}'

class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def __str__(self):
        students = ""
        for student in self.students:
            students = students + '\n'
            students = students + str(student)

        return f'School: {self.name}, with {len(self.students)} students: {students}'

def create_school_with_students(school_name):
    number_of_students = random.randint(1, 20)
    students = []
    for student_number in range(number_of_students):
        first_name = f'Student_{student_number + 1}'
        last_name =  'Smith'
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school

def run_example():
    school = create_school_with_students('Hogwart')
    str_school = str(school)
    print(str_school)
    # print(school)

if __name__ == '__main__':
    run_example()