### Zmienna - nazewnictwo zmiennych, typy zmiennych
#
# Zmienna zawsze pisana jest z małej litery z podkreśleniami - może zmieniać w zależności od potrzeb swoją wartość.
# Stała jest przeciwieństwem zmiennej - pisana jest z dużej litery (również z podkresleniami) i przyjmuje jedną,
# określoną wartość, która później podczas działania programu się nie zmienia (nie powinna ulec zmianie - działanie nieporządane).

# Należy pamiętać, że nie można rozpoczynać nazwy zmiennej od cyfr !


# ZMIENNA - POJEMNIK NA WARTOŚĆ

zmienna = 'zmienna'
number = 5
python_age = 30
name = 'Mikołaj'
same_number = number

print('zmienna', zmienna)
print('same_number', number)
print('python_age', python_age)
print(f'Nazywam się {name}')

# STAŁA - ZMIENNA O OKREŚLONEJ, NIEZMIENIALNEJ WARTOŚCI (RÓWNIEŻ POJEMNIK NA WARTOŚĆ)
CONST_VALID_NAME = 3.14

notValidName = 0
NotValidName = 0
NoTvAlIdNaMe = 0

# LICZBA CAŁKOWITA - 'int'
number = 30
print(number)

# LICZBA UŁAMKOWA (ZMIENNOPRZECINKOWA) - 'float'
number = 2.4556
print(number)

# NAPIS - 'string' lub 'str'
name = 'Mikołaj'
print(name)

# UPORZĄDKOWANA LISTA - 'list'

shopping_list = [
    'chleb',
    'jajka',
    'mąka',
    'chleb',
    'mleko'
]
print(shopping_list)
print(f' Pierwszy element na liście: {shopping_list[0]}')

# UPORZĄDKOWANY SŁOWNIK - ZBIÓR SEKWENCJI PAR: 'klucz' -> 'wartość' JAKO 'dict'
wydatki = {
    'woda': 210,
    'energia': 100,
    'zakupy': [
        55.0,
        21,
        75.49,
        150],
    'rozrywka' : 150
}
print(wydatki)
print(wydatki['zakupy'])

# WARTOŚĆ LOGICZNA 'Prawda' LUB 'Fałsz - TYP 'bool'
true_value = True
false_value = False

print(true_value)
print(false_value)

## Instrukcje warunkowe

income = 5000
employees = 7
years_on_the_market = 3

if income < 5000:
  print('Przyznano główne wsparcie')
elif 5 < employees <= 10:
  print('Przyznano wsparcie z funduszu pracowników')
elif years_on_the_market < 3:
  print('Przyznano wsparcie dla nowych firm')
elif income == 6578:
  print('Przyznano wsparcie niespodziankę')
else:
  print('Przyznano wsparcie na pocieszenie')

## Pętle 'While' oraz 'for'

# PĘTLA 'WHILE':

# PĘTLA 'While' - PĘTLA BĘDZIE TRWAĆ DOPÓKI UŻYTKOWNIK NIE PODA LICZBY PARZYSTEJ

number = 1
while number % 2 != 0:
  number = int(input('Podaj liczbę parzystą: '))

print('Brawo !!!')

# PĘTLA 'FOR':

# PĘTLA 'for' ITERUJE DLA KAŻDEFGO ELEMENTU OBIEKTU WSKAZANEGO

favourite_sports = ['bieganie', 'pływanie', 'jazda na rowerze', 'triathlon']
for sport in favourite_sports:
  print(sport)

# UŻYCIE METODY 'enumerate' DODA NAM INDEKSY DO KAŻDEGO ELEMENTU

favourite_sports = ['bieganie', 'pływanie', 'jazda na rowerze', 'triathlon']
for idx, sport in enumerate(favourite_sports):
  print(idx, sport)

# ITEROWANE PO PARACH 'klucz' -> 'wartość' W SŁOWNIKU

expenditures = {
    'prąd': [250],
    'woda': [30.45],
    'zakupy': [
        120.15,
        170.53,
        20.15
    ]
}

for expenditure_name, expenditure_value in expenditures.items():
  print(expenditure_name, expenditure_value)

# ITEROWANIE PO LITERACH W NAPISIE

name = 'Mikołaj'

for letter in name:
  print(letter)

# WYPISYWANIE KOLEJNYCH LICZB

for number in range(12):
  print(number)

# Instrukcje sterujące w pętli - 'break' oraz 'continue'

# INSTRUKCJA BREAK
# POSZUKIWANIE ELEMENTU W ZBIORZE

expenditures = [120, 300, 240.45, 3000, 50, 75]

for expenditure in expenditures:
  print(expenditure)
  if expenditure > 1000:
    print('Drogi wydatek znaleziony')
    break

# WYPISYWANIE CO DRUGIEGO SPORTU

favourite_sports = ['bieganie', 'pływanie', 'jazda na rowerze', 'triathlon']

for idx, sport in enumerate(favourite_sports):
  if idx % 2 != 0:
    continue
  print(sport)

# Funkcje

def find_best_grades(grades_by_subject):
  best_grade = 0
  for subject, grades in grades_by_subject.items():
    best_grade_from_subject = max(grades)
    if best_grade_from_subject > best_grade:
      best_grade = best_grade_from_subject
  return best_grade

grades_data = {
    'Historia' : [5, 5, 4, 5],
    'Matematyka': [5, 4, 3, 6],
    'Fizyka': [4, 3, 2, 5]
}

the_best_grade = find_best_grades(grades_data)
print(f'Najlepsza uzyskana ocena to {the_best_grade}.')