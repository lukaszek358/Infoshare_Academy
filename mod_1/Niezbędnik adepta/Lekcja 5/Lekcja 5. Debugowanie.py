
# 1. Napisaliśmy program.
# 2. Uruchamiamy program, ale nie działa tak jakbyśmy chcieli.
# 3. Uruchamiamy program (kod) w debugerze i szukamy błędu/ błędów.
# 4. Zaczynamy od 'breakpointa' w podejrzanym miejscu.

# print('Hello World')

def find_best_grades(grades_by_subject):
    best_grade = 0
    for subject, grades in grades_by_subject.items():
        best_grade_from_subject = max(grades)
        if best_grade_from_subject > best_grade:
            best_grade = best_grade_from_subject
    return best_grade


grades_data = {
    'historia': [5, 5, 5, 4],
    'matematyka': [5, 4, 3, 6],
    'fizyka': [4, 3, 3, 5]
}

the_best_grade = find_best_grades(grades_data)
print(f'Najlepsza ocena uzyskana: {the_best_grade}')
