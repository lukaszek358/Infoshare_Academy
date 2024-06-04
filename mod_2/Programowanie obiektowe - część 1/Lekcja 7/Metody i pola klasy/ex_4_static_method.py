import random

class Config:

    ADMINISTRATOR_EMAIL = "admin..."
    SYSTEM_DOMAIN = "..."
    DATABASE_URL = "..."

    RANDOM_FINAL_GRADES_NUMBER = 5
    MIN_RANDOM_GRADE = 1
    MAX_RANDOM_GRADE = 5

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
        if not self.check_promotion():
            self.promoted = False
        else:
            self.promoted = True
    def check_promotion(self):
        return GradeCalculator.check_student_promotion(self._final_grades)

class Grade:
    FAILING_GRADE = 1
    def __init__(self, value):
        self.value = value
    def is_passing(self):
        return self.value > Grade.FAILING_GRADE

class GradeCalculator:
    MAX_FAILED_TO_PASS = 2
    @staticmethod
    def check_student_promotion(final_grades):
        failing_grades = GradeCalculator.get_number_of_failing_grades(final_grades)
        if failing_grades > GradeCalculator.MAX_FAILED_TO_PASS:
            return False
        return True
    @staticmethod
    def get_number_of_failing_grades(grades):
        failing_grades = 0
        for grade in grades:
            if not grade.is_passing():
                failing_grades = failing_grades + 1
        return failing_grades

    @staticmethod
    def calculate_student_avg(final_grades):
        grade_sum = 0
        for grade in final_grades:
            grade_sum = grade_sum + grade.value
        return grade_sum/len(final_grades)
class School:
    MAX_STUDENTS_NUMBER = 20
    def __init__(self, name, students):
        self.name = name
        self.students = students
        # self._promote_lucky_students()
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
    def create_school_with_students(cls, school_name):
        number_of_students = random.randint(1, cls.MAX_STUDENTS_NUMBER)
        school = School(school_name, students=[])

        for student_number in range(number_of_students):
            first_name = f"Student-{student_number}"
            last_name = "Smith"
            student = Student(first_name, last_name)
            school.assign_student(student)
            for _ in range(Config.RANDOM_FINAL_GRADES_NUMBER):
                final_grade = random.randint(Config.MIN_RANDOM_GRADE, Config.MAX_RANDOM_GRADE)
                student.add_final_grade(final_grade)
        return school
    def assign_student(self, student):
        # if len(self.students) < School.MAX_STUDENTS_NUMBER:
        if len(self.students) < self.MAX_STUDENTS_NUMBER:
            self.students.append(student)
        else:
            print('Nie ma już w szkole miejsc!')

def run_example():
    school = School.create_school_with_students('Hogwart')
    print(school)

if __name__ == '__main__':
    run_example()