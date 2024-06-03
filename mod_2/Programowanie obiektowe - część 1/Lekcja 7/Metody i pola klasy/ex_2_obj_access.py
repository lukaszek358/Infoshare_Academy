# DOSTĘP DO METODY I OBIEKTU KLASY
import random
class Grade:
    FAILING_GRADE = 1

    def __init__(self, value):
        self.value = value
    def is_passing(self):
        return self.value > Grade.FAILING_GRADE
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self._final_grades = []
    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}, Promoted: {self.promoted}'
    def promote(self):
        self.promoted = True
    def add_final_grade(self, grade):
        self._final_grades.append(Grade(value= grade))
        if grade == 1:
            self.promoted = False
class School:
    MAX_STUDENTS_NUMBER = 20                # ZMIENNA KLASY (JEST TO STAŁA [NIEZMIENNA] - PISANA JEST Z WIELKICH LITER)
    def __init__(self, name, students):
        self.name = name
        self.students = students
        self._promote_lucky_students()
    def _promote_lucky_students(self):
        for index, student in enumerate(self.students):
            if index % 3 == 0:
                student.promote()
    def __str__(self):
        students = ''
        for student in self.students:
            students = students + '\n'
            students = students + str(student)
        return f'School: {self.name} with {len(self.students)} students : {students}'

    @classmethod
    # ADNOTACJA METODY WEWNĄTRZ KLASY - DEKORATOR TEN OZNACZA, ŻE NIE JEST TO ZWYKŁA METODA
    # OKREŚLA, ŻE TA METODA PRZYPISANA JEST DO KONKRETNEJ KLASY A NIE DO CAŁEGO OBIEKTU
    def create_school_with_students(cls, school_name):
        number_of_students = random.randint(1, cls.MAX_STUDENTS_NUMBER)
        students = []
        for student_number in range(number_of_students):
            first_name = f'Student_{student_number + 1}'
            last_name = f'Smith'
            students.append(Student(first_name, last_name))
        school = School(school_name, students)
        return school
    def assign_student(self, student):
        # if len(self.students) < School.MAX_STUDENTS_NUMBER:
        if len(self.students) < self.MAX_STUDENTS_NUMBER:
            self.students.append(student)
        else:
            print('Nie ma już w szkole miejsc!')
def run_example():
    school = School.create_school_with_students('Hogwart')
    harry = Student(first_name= 'Harry', last_name= 'Potter')
    school.assign_student(harry)
    print(school)

    new_school = School.create_school_with_students('Nowa Szkoła')

    print(f'Hogwart może mieć maksymalnie {school.MAX_STUDENTS_NUMBER} ucznów')
    print()
    print(f'Nowa Szkoła może mieć maksymalnie {new_school.MAX_STUDENTS_NUMBER} ucznów')

if __name__ == '__main__':
    run_example()