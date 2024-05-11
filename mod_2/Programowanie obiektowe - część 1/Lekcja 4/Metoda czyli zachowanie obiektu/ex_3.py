import random
from estudent.school_1 import School, create_school_with_students
from estudent.student_1 import Student_1

def run_example():
    school = create_school_with_students('Griffindor')

    for student in school.students:
        student.promote()
    school.print_self()
    print("=o=" * 40)

    for student in school.students:
        final_grade = random.randint(1, 5)
        student.add_final_grade(final_grade)
    school.print_self()

if __name__ == '__main__':
    run_example()