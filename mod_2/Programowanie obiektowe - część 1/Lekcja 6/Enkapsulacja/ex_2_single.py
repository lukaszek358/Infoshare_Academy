# POJEDYŃCZE PODKREŚLENIE ('_') PRZED METODĄ LUB KLASĄ JEST DEKLARACJĄ, ŻE NIE CHCEMY BY DANA METODA/ATRYBUT BYŁ WYKORZYSTYWANY POZA OBIEKTEM
# POLE NADAL BEDZIE WIDOCZNE I MOŻLIWE DO MODYFIKACJI
import random
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students
        self._promote_lucky_students()
    def _promote_lucky_students(self):
        for index, student in enumerate(self.students):
            if index % 3 == 0:
                student.promote()
    def __str__(self):
        students = ""
        for student in self.students:
            students += "\n"
            students += str(student)

        return f"School: {self.name}, with {len(self.students)} students: {students}"
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self._final_grades = []
    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, promoted: {self.promoted}"
    def promote(self):
        self.promoted = True
    # def add_final_grade(self, grade):
    #     self._final_grades.append(grade)
    #     if grade == 1:
    #         self.promoted = False
    def add_final_grade(self, grade):
        self._final_grades.append(Grade(value=grade))
        if grade == 1:
            self.promoted = False
class Grade:
    def __init__(self, value):
        self.value = value
    def is_passing(self):
        return self.value > 1

def create_school_with_students(school_name):
    number_of_students = random.randint(1, 20)
    students = []
    for student_number in range(number_of_students):
        first_name = f"Student-{student_number}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school

def run_example():
    school = create_school_with_students("Hogwart")
    student = school.students[0]
    student.add_final_grade(4)

    print(student._final_grades)
    school._promote_lucky_students()

if __name__ == '__main__':
    run_example()