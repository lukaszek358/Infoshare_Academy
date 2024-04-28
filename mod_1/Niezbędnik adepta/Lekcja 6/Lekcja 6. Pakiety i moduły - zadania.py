# # Zadanie nr 1
# # Napisz funkcję obliczającą średnią prędkość biegu na podstawie czasu i pokonanego dystansu (prędkość = dystans / czas).
# # Umieść ją w jednym pliku.W drugim pliku zaimportuj moduł, wczytaj informacje od użytkownika
# # i wywołaj funkcję - oblicz prędkość średnią.
#
# from source_root import funkcje_import
#
# distance = float(input("Podaj jaki pokonałeś dystans: "))
# time_in_hours = int(input(f'Podaj ile czasu (w godzinach) zajeło Ci pokonanie dystansu {distance} kilometrów: '))
#
# avg = funkcje_import.average_speed(distance, time_in_hours)
#
# print(f'Poruszałeś się z prędkością {avg:.2f} km/h')
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Zadanie nr 2
#
# Zaimplementuj funkcję obliczającą długość przeciwprostokątnej trójkąta na podstawie otrzymanych długości przyprostokątnych.
# Wzór to: c = pierwiastek_z(a ^ 2 + b ^ 2), gdzie c to przeciwprostokątna.
# Wykorzystaj w tym celu moduł math z biblioteki standardowej oraz funkcje:
#     * sqrt(x) - liczy pierwiastek drugiego stopnia z podanej wartości x
#     * pow(x, y) - podnosi x do potęgi y

# from source_root import funkcje_import
#
# a_side = float(input('Podaj długość pierwszej przyprostokątnej (w cm): '))
# b_side = float(input('Podaj długość drugiej przyprostokątnej (w cm): '))
#
# c_value = funkcje_import.pitagoras_traingle(a_side, b_side)
# print(f'Długość przeciwprostokątnej wynosi {c_value:.2f} cm dla trójkąta o przyprostkoątnych: {a_side} oraz {b_side} cm')
# # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Zadanie nr 3
#
# Napisz kalkulator obliczający wartość lokaty po pewnym czasie.# Wczytaj od użytkownika informacje o:
#     Początkowym kapitale (wpłaconej kwocie)
#     Oprocentowaniu
#     Okresie trwania inwestycji (w latach)
#
# Umieść funkcję obliczająca wartość lokaty w pakiecie calculations, a wczytanie danych i uruchomienie obliczeń w pliku powyżej pakietu.
# Skorzystaj ze wzoru: wartość = wartość pocz. * (1 + procent/100) ^ liczba lat
#
#
# from calculations import investment_import
# def ask_for_int_value(message):
#     input_value = input(message)
#     return int(input_value)
#
# initial_value = ask_for_int_value('Jaką kwotę chcesz wpłacić na lokatę: ')
# percentage = ask_for_int_value('Jakie jest oprocentowanie (%) na lokacie: ')
# years = ask_for_int_value('Ile lat trwa lokata: ')
#
# investment_value = investment_import.calculate_investment_value(initial_value, percentage, years)
#
# if years == 1:
#     print(f'Wartość Twojej lokaty po roku wyniesie {investment_value:.2f}')
# else:
#     print(f'Wartość Twojej lokaty po {years} latach wyniesie {investment_value:.2f} PLN')
