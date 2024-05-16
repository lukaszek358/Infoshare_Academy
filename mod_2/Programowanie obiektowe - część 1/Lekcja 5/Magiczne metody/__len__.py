# METODA __len__ SŁUŻY DO OBSŁUŻENIA FUNKCJI WBUDOWANEJ len()
# METODA __len__ ZWRACA LICZBĘ CAŁKOWITĄ REPREZENTUJĄCĄ DŁUGOŚĆ NASZEGO OBIEKTU (O ILE JEST TO MOŻLIWE)

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

    def __len__(self):
        return len(self.students)

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
    len_school = len(school)
    print(len_school)

if __name__ == '__main__':
    run_example()