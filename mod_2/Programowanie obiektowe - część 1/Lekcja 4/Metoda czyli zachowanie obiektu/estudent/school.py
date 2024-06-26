import random
from estudent.student import Student

class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students
        self. promote_lucky_students()

    def promote_lucky_students(self):
        for idx, student in enumerate(self.students):
            if idx % 3 == 0:
                student.promote()

    def print_self(self):
        print(f'School: {self.name}, with {len(self.students)} students')
        for student in self.students:
            student.print_self_student()

def create_school_with_students(school_name):
    number_of_students = random.randint(1, 20)
    students = []
    for student_number in range(number_of_students):
        first_name = f'Student_{student_number + 1}'
        last_name = 'Smith'
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school