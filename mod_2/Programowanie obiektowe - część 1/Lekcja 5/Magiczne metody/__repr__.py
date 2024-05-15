# METDOA __repr__ JEST BARDZO PODOBNA DO METODY __str__
# METDOA __repr__ MA ZA ZADANIE ZWRÓCIĆ NAM 'OFICJALNĄ' REPREZENTACJĘ NASZEGO OBIKETU
# W TEJ METODZIE 'OFICJALNA' REPREZENTACJA MA ZA ZADANIE PRZEKAZAĆ NAM WSZELKIE UŻYTECZNE INFORMACJE NA TEMAT OBIEKTU

import random
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

    def __repr__(self):                                                                                                 # METODA __repr__
        return f'<Student first_name = {self.first_name}, last_name = {self.last_name}, promoted = {self.promoted}> '
    def __str__(self):                                                                                                  # METODA __str__
        return f'Student: {self.first_name} {self.last_name}, Promoted: {self.promoted}'

class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def __repr__(self):
        students_reprs = []
        for student in self.students:
            students_reprs.append(repr(student))
        all_students_repr = ','.join(students_reprs)
        return f'<School name = {self.name}, students = [{all_students_repr}]>'

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
    school_repr = repr(school)
    print(school_repr)

if __name__ == '__main__':
    run_example()