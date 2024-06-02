# ENKAPSULACJA - JEST TO PRAWO DO PRYWATNOŚCI DANEGO OBIEKTU W KONTEKŚCIE DANEJ KLASY
# PRAWO, BY CZĘŚĆ JEGO DANYCH CZY SZCZEGÓŁY W JAKI SPOSÓB REALIZUJE ON JAKIEŚ ZACHOWANIE (ZA POMOCĄ KODU) NALEŻAŁY TYLKO DO NIEGO
# STAN KLASY (OBIEKTU) NIE MOŻE BYĆ MODYFIKOWANY Z ZEWNĄTRZ PRZEZ JAKIEŚ INNE FUNKCJE I OBIEKTY
# STAN OBIEKTU/ KLASY MOŻE BYĆ MODYFIKOWANY TYLKO POPRZEZ WYWOŁANIE METODY WEWNĄTRZ SIEBIE JAKO KLASA/OBIEKT

# DZIEKI TEMU OBIEKT MA KONTROLE NAD SWOIM STANEM I ZAPEWNIA JEGO SPÓJNOŚĆ

import random
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students
        self.promote_lucky_students()
    def promote_lucky_students(self):
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
        self.final_grades = []
    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, promoted: {self.promoted}"
    def promote(self):
        self.promoted = True
    def add_final_grade(self, grade):
        self.final_grades.append(grade)
        if grade == 1:
            self.promoted = False
    # def add_final_grade(self, grade):
    #     self.final_grades.append(Grade(value=grade))
    #     if grade == 1:
    #         self.promoted = False
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

def final_grades_no_encapsulation(school):                                                                              # ABSTRAKCJA
    for student in school.students:
        final_grade = random.randint(1, 5)
        student.final_grades.append(final_grade)
    print(school)

def final_grades_with_encapsulation(school):                                                                            # ENKAPSULACJA
    for student in school.students:
        final_grade = random.randint(1, 5)
        student.add_final_grade(final_grade)
    print(school)


def run_example():
    school = create_school_with_students("Hogwart")

    for student in school.students:
        student.promote()
    # print(school)
    # print("=" * 20)

    final_grades_no_encapsulation(school)
    print("=" * 20)
    final_grades_with_encapsulation(school)


if __name__ == '__main__':
    run_example()