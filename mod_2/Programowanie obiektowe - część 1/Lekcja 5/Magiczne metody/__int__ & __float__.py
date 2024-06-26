# METODA __int__ ORAZ METODA __float__ MAJĄ ZA ZADANIE ZWRACAĆ REREZENTACJĘ OBIEKTU POD POSTACIĄ LICZBOWĄ
# DOMYŚLNA IMPLEMENTACJA TYCH METODA ZWRACA BŁĄD - NIE KAŻDA KLASA JEST ZAMIENIALNA NA POSTAĆ LICZBOWĄ (I MA SENS)
# IMPLEMENTACJA TYCH METOD NIE JEST MOŻLIWA DLA WSZYSTKICH KLAS TAK JAK W PRZYPADKU METODY __repr__ LUB __str__
# POWINNY ZWRACAĆ LICZBY DANEGO TYPU Z METODY

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

    def __int__(self):
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
    int_school = int(school)
    print(int_school)

if __name__ == '__main__':
    run_example()