# # ODPOWIEDZIALNOŚCIĄ KONSTRUKTORA JEST INICJALIZACJA STANU OBIEKTU
# # KONSTRUKTOR ZAWSZE JEST WYWOŁYWANY AUTOMATYCZNIE W MOMENCIE TWORZENIA NOWEGO OBIKETU/ NOWEJ INSTANCJI
#
# class Student:
#     # pass
#     def __init__(self):
#         print('Tworzenie nowej instancji - powstaje nowy obiekt')
#
# if __name__ == '__main__':
#     student = Student()
# #-----------------------------------------------------------------------------------------------------------------------
#
# # ZADANIEM KONSTRUKTORA JEST ZDEFINIOWAĆ I ZINICJALIZOWAĆ STAN OBIEKTU
# class Student:
#     def __init__(self):
#         self.first_name = 'Mikołaj'
#         self.last_name = 'Lewandowski'
#         self.age = 54
# def run_example():
#     student = Student()
#
#     # DO STANU OBIKETU MAMY DOSTĘP - MOŻEMY GO ODCZYTAĆ
#     print(student.first_name)
#     print(student.last_name)
#     print(student.age)
#
# #-----------------------------------------------------------------------------------------------------------------------
# # STAN OBIEKTU MOŻEMY RÓWNIEŻ MODYFIKOWAĆ
# class Student:
#     def __init__(self):
#         self.first_name = 'Mikołaj'
#         self.last_name = 'Lewandowski'
#         self.age = 54
#
# def run_example():
#     student = Student()
#
#     student.first_name = 'Łukasz'
#     student.last_name = 'Markowski'
#     student.age = 32
#     print(student.first_name)
#     print(student.last_name)
#     print(student.age)
# #-----------------------------------------------------------------------------------------------------------------------
# # KONSTRUKTOR MOŻE PRZYJĄĆ RÓWNIEŻ ARGUMENTY - JAK FUNKCJA:
# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.promoted = False
#
# def print_student(student):
#     print(f'Student: {student.first_name}, {student.last_name}, promoted: {student.promoted}')
#
# # W FUNKCJI MOŻEMY ZMODYFIKOWAĆ STAN OBIEKTU (TZW. side effect)
# def promote_student(student):
#     student.promoted = True
#
# def run_example():
#     student = Student(first_name = 'Ola', last_name = 'Nowak')
#     print_student(student)
#
#     other_student = Student(first_name= 'Jerzy', last_name= 'Jurkowski')
#     print_student(other_student)
#
#     promote_student(student)
#     print_student(student)

# #-----------------------------------------------------------------------------------------------------------------------
# import random
#
# # OBIEKT MOŻE ZAWIERAĆ W SOBIE INNE OBIEKTY
# class School:
#     def __init__(self, name, students):
#         self.name = name
#         self.students = students
# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.promoted = False
#
# def print_student(student):
#     print(f'Student: {student.first_name}, {student.last_name}, promoted: {student.promoted}')
#
# # W FUNKCJI MOŻEMY ZMODYFIKOWAĆ STAN OBIEKTU (TZW. side effect)
# def promote_student(student):
#     student.promoted = True
#
# # FUNKCJA MOŻE ZWRACAĆ OBIEKTY
# def create_school_with_students(school_name):
#     number_of_students = random.randint(1, 20)
#     students = []
#     for student_number in range(number_of_students):
#         first_name = f'Student-{student_number}'
#         last_name = 'Smith'
#         students.append(Student(first_name, last_name))
#     school = School(school_name, students)
#     return school
#
# def run_example():
#     school = create_school_with_students('Hogwart')
#     print(school)
#     for student in school.students:
#         print_student(student)
##----------------------------------------------------------------------------------------------------------------------
# #KONSTRUKTOR NIE MUSI 'WPROST' PRZYPISYWAĆ PRZEKAZANYCH WARTOŚCI, MOŻĘ WYKONAĆ SWOJĄ LOGIKĘ
# class School:
#     def __init__(self, name, students):
#         self.name = name
#         if len(students) > 10:
#             students = students[:10]
#         self.students = students
#
# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.promoted = False
#
# def print_student(student):
#     print(f'Student: {student.first_name} {student.last_name}, promoted: {student.promoted}')
#
# def create_school_with_students(school_name, number_of_students):
#     students = []
#     for student_number in range(number_of_students):
#         first_name = f'Student-{student_number}'
#         last_name = 'Smith'
#         students.append(Student(first_name, last_name))
#     school = School(school_name, students)
#     return school
#
# def run_example():
#     school = create_school_with_students('Hogwart', 40)
#     print(school)
#     for student in school.students:
#         print_student(student)
##----------------------------------------------------------------------------------------------------------------------
# #KONSTRUKTOR Z DOMYŚLNYM ARGUMENTEM  - UWAGA MA DOMYŚLNĄ LISTĘ
# class School:
#     def __init__(self, name, students = None):
#         self.name = name
#         if students is None:
#             students = []
#         self.students = students
# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.promoted = False
#
# def print_student(student):
#     print(f'Student: {student.first_name} {student.last_name}, promoted: {student.promoted}')
#
# # UWAGA! Ponownie 'side effect'
# def assign_student_to_school(school, student):
#     school.students.append(student)
#
# def run_example():
#     empty_school = School('Pusta szkoła')
#     first_student = Student(first_name= 'Jakub', last_name= 'Kowalski')
#     assign_student_to_school(empty_school, first_student)
#     for student in empty_school.students:
#         print_student(student)
##----------------------------------------------------------------------------------------------------------------------
# Z KONSTRUKTORA MOŻEMY WYWOŁYWAĆ INNE FUNKCJE
import random
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students
        promote_lucky_students(students)
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

def print_student(student):
    print(f'Student: {student.first_name} {student.last_name}, promoted: {student.promoted}')

def promote_lucky_students(students):
    for idx, student in enumerate(students):
       if idx % 3 == 0:
           promote_student(student)
def promote_student(student):
    student.promoted = True

def create_school_with_students(school_name):
    number_of_students = random.randint(1, 20)
    students = []
    for student_number in range(number_of_students):
        first_name = f'Student-{student_number}'
        last_name = 'Smith'
        students.append(Student(first_name, last_name))
    school = School(school_name, students)
    return school

def run_example():
    school = create_school_with_students('Hogwart')
    print(school)
    for student in school.students:
        print_student(student)
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    run_example()
