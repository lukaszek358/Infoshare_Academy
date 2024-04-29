# PARADYGMAT PROGRAMOWANIA - STYL/ SPOSÓB PROGRAMOWANIA:

# IMPERATYWNY - DOKŁADNE DEFINIOWANE PRZEPŁYWU PROGRAMU I SEKWENCJI KOMEND DO WYKONANIA,
# DEKLARATYWNY - DEFINIOWANY EFEKT JAKI CHCEMY UZYSKAĆ, NP. SQL
# PROCEDURALNY - IMPERATYWNY + WYKORZYSTYWANE REUŻYWALNE PROCEDURY (NP. STOSOWANIE FUNKCJI W RÓZNYCH MIEJSCACH KODU),
# OBIEKTOWY - PRGRAM JAKO ZBIÓR OBIEKTÓW (O RÓŻNYCH CECHACH I ZACHOWANIACH) KOMUNIUJĄCYCH SIĘ ZE SOBĄ
# FUNKCYJNY,
# ASPEKTOWY - OBSŁUZENIE SIĘ PRZECINAJĄCYCH SIĘ KONCEPTÓW
# ZDARZENIOWY


# KONCEPCJE PROGRAMOWANIA OBIEKTOWEGO:

# ENKAPSULACJA - INACZEJ PRAWO DO PRYWATNOŚCI,
# ABSTRAKCJA - POSTRZEGANIE LEMENTÓW PROGRAMÓW W BARDZIEJ OGÓLNY SPOSÓB, BEZ DEFINIOWANIA SZCZEGÓŁÓW,
# DZIEDZICZENIE
# KOMPOZYCJA - BYCIE CZĘŚCIĄ 'CZEGOŚ'
# POLIMORFIZM - NIE PRZEJMOWANIE SIE JAKIEGO TYPU JEST DANY OBIEKT, KTÓREGO UŻYWAMY

#----------------------------------------------------------------------------------------------------------------------#

class Student:
    pass                                           # CIAŁO KLASY + 'pass' (OZNACZA 'NIC', ŻADNEJ CZYNNOŚCI DO WYKONANIA)

class Grade:
    pass

class School:
    pass

if __name__ == '__main__':
    student_mikolaj = Student()                     #TWORZENIE INSTANCJI OBIEKTU / KLASY

    grade_a = Grade()
    grade_f = Grade()

    my_school = School()

    # print(student_mikolaj)
    # print(grade_a, grade_f)
    # print(my_school)

    # print('student_mikolaj: ', type(student_mikolaj))
    # print('grade_a: ', type(grade_a))
    # print('grade_f: ', type(grade_f))
    # print('my_school: ', type(my_school))

    all_students = [Student(), Student(), Student(), Student(), Student()]
    print(all_students)
    print(all_students[0])

    grades = {
        1: Grade(),
        2: Grade(),
        3: Grade(),
        4: Grade(),
        5: Grade(),
        6: Grade(),
    }

    print()
    print(grades)