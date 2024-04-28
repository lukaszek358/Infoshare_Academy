# # KOD MOŻNA PODZIELIĆ NA MNIEJSZE FRAGMENTY - TZW. MODUŁY
# # MODUŁ TO SPÓJNY KAWAŁEK NASZEGO SYSTEMU
# # MODUŁ TO JEDNOSTKA, W KTÓREJ ORGANIZUJEMY SWÓJ KOD
#
#
# # IMPORTUJEMY FUNKCJONALNOŚĆ Z PLIKU 'hello_world'
# # IMPORTUJEMY MODUŁ 'import_test' - JEST ON DOSTĘPNY W TYM PLIKU
#
# from source_root import import_test
#
# # ZA POMOCĄ KROPKI MOŻEMY ODWOŁAĆ SIĘ DO KONKRETNYCH FUNKCJI I ZMIENNYCH DOSTĘPNYCH W IMPORTOWANYM PLIKU
#
# import_test.say_hello()
#
# name = input('Jak się nazywasz?')
# import_test.say_hello_with_name(name)

# # MECHANIZM IMPORTOWANIA:
# # 1 . Przeszukanie znanym lokalizacji
# # 2. Zapisanie informacji o module
# # 3. Załadowanie modułu
# # 4. Udostępnienie pod odpowiednią nazwą
#
# # KOLEJNOŚĆ POSZUKIWANIA MODUŁÓW:
# # 1. Lista wcześniej wczytanych modułów
# # 2. Biblioteka startowa
# # 3. Katalog uruchomienia skryptu
# # 4. PYTHONPATH
# # 5. Zainstalowane zewnętrzne biblioteki

# WBUDOWANA BIBLIOTEKA STANDARDOWA 'math' ZAWIERE WIELE PRZYDATNYCH NARZĘDZI

# import math
#
# # STAŁA 'pi'
# print('pi: ' , round(math.pi, 4))
#
# # FUNKCJA SINUS
# sinus_180 = math.sin(math.pi)
# print('sinus_180: ', sinus_180)
#
# # NIESKOŃCZONOŚĆ
# print('math.inf:', math.inf)
#
# # ZAPIS Z DOLNYM PODKREŚLENIEM JEST TAKI SAM JAK TEMU BEZ - WPŁYWA TO NA CZYTELNOŚĆ
#
# very_big_number = 100_000_000_000
# the_biggest_number = math.inf
#
# #NIESKOŃCZONOŚĆ JEST WIĘKSZA NIZCOKOLWIEK INNEGO
# print('the_biggest_number > very_big_number: ', the_biggest_number > very_big_number)