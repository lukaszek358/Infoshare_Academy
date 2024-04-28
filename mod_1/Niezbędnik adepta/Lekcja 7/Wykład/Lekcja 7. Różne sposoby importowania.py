#
# # # WYWOŁYWANIE FUNKCJI Z PAKIETU WIĄŻE SIĘ Z OKREŚLONĄ DŁUGOŚCIĄ ZAPISU
# # # IM BARDZIEJ ZAGNIEŻDŻONA FUNKCJA — DŁUŻSZY BĘDZIE ZAPIS WYWOŁYWANIA
# #
# # # ZA POMOCĄ from... import MOŻEMY IMPORTOWAĆ ZARÓWNO CAŁY MODUŁ JAK I POJEDYŃCZE FUNKCJE/ ZMIENNE
# #
# from school import promotion_status
# from school.grade_calculator import calculate_student_final_grades
# from school.promote import check_promotion
# from school.students_data import is_student_in_school
#
# print('Witaj w elektronicznym dzienniku!')
#
# student_name = input('Podaj imię ucznia by wiedzieć, czy zdał do kolejnej klasy: ')
#
# if not is_student_in_school(student_name):
#     print(f'Niestety {student_name} nie ma na liście...')
# else:
#     final_grades = calculate_student_final_grades(student_name)
#     promotion_result = check_promotion(final_grades)
#
#     if promotion_result == promotion_status.PASSED:
#         print(f'Gratulacje, {student_name} zdał do następnej klasy!')
#     elif promotion_result == promotion_status.FAILED:
#         print(f'Niestety, {student_name} nie zdał ...')
#     else:
#         print('Coś poszło nie tak - zgłoś obsłudze systemu')
#
# #----------------------------------------------------------------------------------------------------------------------#
#
# ## W PLIKU '_init_' MOŻEMY OZNACZYĆ CO MOŻEMY IMPORTOWAĆ W MOMENCIE UŻYCIA 'import *' CZYLI IMPORTOWANIA WSZYSTKIEGO
# ## DO ZMIENNEJ '__all__' JAKO LISTĘ PODAJEMY PAKIETY (NP. __all__ = ['promote']), KTÓRE MAJĄ BYĆ IMPORTOWANE PRZY UŻYCIU 'import *'
# ## JEŻELI NIE MAMY OKRESLONEJ ZMIENNEJ '__all__' TO ZOSTANĄ ZAIMPORTOWANE PAKIETY, KTÓRE IMPORTUJEMY BEZPOŚREDNIO DO PLIKU '_init_'
# # from school import *
# #
# # print('Witaj w elektronicznym dzienniku!')
# #
# # student_name = input('Podaj imię ucznia by wiedzieć, czy zdał do kolejnej klasy: ')
# #
# # if not is_student_in_school(student_name):
# #     print(f'Niestety {student_name} nie ma na liście...')
# # else:
# #     final_grades = calculate_student_final_grades(student_name)
# #     promotion_result = check_promotion(final_grades)
# #
# #     if promotion_result == promotion_status.PASSED:
# #         print(f'Gratulacje, {student_name} zdał do następnej klasy!')
# #     elif promotion_result == promotion_status.FAILED:
# #         print(f'Niestety, {student_name} nie zdał ...')
# #     else:
# #         print('Coś poszło nie tak - zgłoś obsłudze systemu')
#
# ##---------------------------------------------------------------------------------------------------------------------#
#
# # ZA POMOCĄ import... as MOŻEMY ZAIMPORTOWAĆ MODUŁ POD INNĄ NAZWĄ
#
# from school import promotion_status as status
#
# print('Witaj w elektronicznym dzienniku!')
#
# student_name = input('Podaj imię ucznia by wiedzieć, czy zdał do kolejnej klasy: ')
#
# if not is_student_in_school(student_name):
#     print(f'Niestety {student_name} nie ma na liście...')
# else:
#     final_grades = calculate_student_final_grades(student_name)
#     promotion_result = check_promotion(final_grades)
#
#     if promotion_result == status.PASSED:
#         print(f'Gratulacje, {student_name} zdał do następnej klasy!')
#     elif promotion_result == promotion_status.FAILED:
#         print(f'Niestety, {student_name} nie zdał ...')
#     else:
#         print('Coś poszło nie tak - zgłoś obsłudze systemu')
