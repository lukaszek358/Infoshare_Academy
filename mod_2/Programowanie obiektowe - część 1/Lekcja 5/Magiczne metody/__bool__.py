# # METODA __bool__ JEST WYKORZYSTYWANE DO KONWERSJI OBIEKTU NA TYP boolean (INACZEJ True/ False)
# # WYWOŁUJE FUNKCJE WBUDOWANĄ bool() I ZWRACA WARTOŚĆ JAKO True/ False
#
# import random
# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.promoted = False
#
#     def __bool__(self):
#         return self.promoted
#
# def run_example():
#     student = Student(first_name= 'Mikołaj', last_name= 'Lewandowski')
#     print(bool(student))
#
#     student.promoted = True
#     print(bool(student))
#
#     if student:
#         print('If student')
#
#     student.promoted = False
#     if student:
#         print(student)

#-----------------------------------------------------------------------------------------------------------------------

# W PRZYPADKU BRAKU OBECNOŚCI W KLASIE METODY __bool__ AUTOMATYCZNIE ZOSTANIE PRZYWOŁYWANA METDOA __len__
# W MOMENCIE KIEDY METODA __len__ ZWRÓCI WARTOŚĆ 0 TO EFEKTEM BĘDZIE WARTOŚĆ 'False', W POZOSTAŁYCH PRZYPADKACH 'True'
# KIEDY KLASA NIE IMPLEMENTUJE ANI METODY __len__, ANI METODY __bool__ TO EFEKTEM ZAWSZE BĘDZIE WARTOŚĆ 'True'
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

    # def __len__(self):
    #     return len(self.students)

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
    school.students = []
    print(bool(school))

if __name__ == '__main__':
    run_example()