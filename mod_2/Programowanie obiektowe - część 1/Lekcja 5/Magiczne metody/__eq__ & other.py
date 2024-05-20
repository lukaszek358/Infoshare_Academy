# # METODY PORÓWNANIA: == '__eq__', != __ne__, < '__lt__, >__gt__, <= '__le__', >= '__ge__'
# # WARTOŚĆ ZWRACANA Z OKREŚLONEJ METODY TRAKTOWANA JEST JAKO WYNIK PORÓWNANIA
# # METODY PORÓWNANIA ZAWSZE POWINNY ZWRACAĆ WARTOŚCI True/False ALBO SPECJALNĄ WARTOŚĆ WBUDOWANĄ ('not implemented')
# ## WARTOŚĆ 'not implemented' INFORMUJE O BRAKU MOŻLWIOŚĆI PORÓWNANIA WARTOŚĆI (NP. OBIKETY RÓŻNYCH KLAS)
#
# class Money:
#     def __init__(self, dollars, cents):
#         self.dollars = dollars
#         self.cents = cents
#
#     def as_cents(self):
#         return self.dollars * 100 + self.cents
#     def __str__(self):
#         return f'{self.dollars}$ and {self.cents} cents'
#
#     def __eq__(self, other):
#         if self.__class__ != other.__class__:
#             return  NotImplemented
#         return self.as_cents() == other.as_cents()
#
#     # # JEŚLI WYŁĄCZYMY METODE '__ne__' I TAK UZYSKAMY WYNIK - ODWOŁA SIĘ DO '__eq__' (METODA PRZECIWNA DO '__ne__')
#     # def __ne__(self, other):
#     #     if self.__class__ != other.__class__:
#     #         return  NotImplemented
#     #     return self.as_cents() != other.as_cents()
#     def __lt__(self, other):
#         if self.__class__ != other.__class__:
#             return  NotImplemented
#         return self.as_cents() < other.as_cents()
#     def __le__(self, other):
#         if self.__class__ != other.__class__:
#             return  NotImplemented
#         return self.as_cents() <= other.as_cents()
#     def __gt__(self, other):
#         if self.__class__ != other.__class__:
#             return NotImplemented
#         return self.as_cents() > other.as_cents()
#     def __ge__(self, other):
#         if self.__class__ != other.__class__:
#             return NotImplemented
#         return self.as_cents() >= other.as_cents()
#
# def run_example():
#     print(f"{Money(dollars=1, cents=20)} == {Money(dollars=100, cents=5)}?")
#     print(Money(dollars=1, cents=20) == Money(dollars=100, cents=5))
#
#     print(f"{Money(dollars=100, cents=5)} == {Money(dollars=100, cents=5)}?")
#     print(Money(dollars=100, cents=5) == Money(dollars=100, cents=5))
#
#     print(f"{Money(dollars=100, cents=5)} != {Money(dollars=100, cents=5)}?")
#     print(Money(dollars=100, cents=5) != Money(dollars=100, cents=5))
#
#     print(f"{Money(dollars=1, cents=20)} < {Money(dollars=100, cents=5)}?")
#     print(Money(dollars=1, cents=20) < Money(dollars=100, cents=5))
#
#     print(f"{Money(dollars=1, cents=20)} <= {Money(dollars=100, cents=5)}?")
#     print(Money(dollars=1, cents=20) <= Money(dollars=100, cents=5))
#
#     print(f"{Money(dollars=1, cents=20)} > {Money(dollars=100, cents=5)}?")
#     print(Money(dollars=1, cents=20) > Money(dollars=100, cents=5))
#
#     print(f"{Money(dollars=1, cents=20)} >= {Money(dollars=100, cents=5)}?")
#     print(Money(dollars=1, cents=20) >= Money(dollars=100, cents=5))

## SPRAWDZAMY CZY KONKRETNY OBIEKT ZNAJDUJE SIĘ NA LIŚCIE OBIEKTÓW ('some_money')
#     print('Sprawdzanie listy "some_money":')
#     some_money = [
#         Money(dollars=1, cents=20),
#         Money(dollars=10, cents=20),
#         Money(dollars=100, cents=20),
#         Money(dollars=1000, cents=20),
#         Money(dollars=10000, cents=20),
#     ]
#     print(f"{Money(dollars=1, cents=20)} in some_money?")
#     print(Money(dollars=1, cents=20) in some_money)
#
#     print(f"{Money(dollars=55, cents=20)} in some_money?")
#     print(Money(dollars=55, cents=20) in some_money)
#
# if __name__ == '__main__':
#     run_example()

##----------------------------------------------------------------------------------------------------------------------
## ALGORYTM PRÓWNYWANIA DWÓCH LIST - DODANY JAKO FUNKCJA I ZAIMPLEMENTOWANY W KODZIE

class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def as_cents(self):
        return self.dollars * 100 + self.cents
    def __str__(self):
        return f'{self.dollars}$ and {self.cents} cents'

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return  NotImplemented
        return self.as_cents() == other.as_cents()

    # JEŚLI WYŁĄCZYMY METODE '__ne__' I TAK UZYSKAMY WYNIK - ODWOŁA SIĘ DO '__eq__' (METODA PRZECIWNA DO '__ne__')
    def __ne__(self, other):
        if self.__class__ != other.__class__:
            return  NotImplemented
        return self.as_cents() != other.as_cents()
    def __lt__(self, other):
        if self.__class__ != other.__class__:
            return  NotImplemented
        return self.as_cents() < other.as_cents()
    def __le__(self, other):
        if self.__class__ != other.__class__:
            return  NotImplemented
        return self.as_cents() <= other.as_cents()
    def __gt__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.as_cents() > other.as_cents()
    def __ge__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.as_cents() >= other.as_cents()


def comprare_money_list(first, second):
    for money in first:
        if money not in second:
            return False
        return  True
def run_example():

    some_money = [
        Money(dollars=1, cents=20),
        Money(dollars=10, cents=20),
        Money(dollars=100, cents=20),
        Money(dollars=1000, cents=20),
        Money(dollars=10000, cents=20),
    ]
    print(f"{Money(dollars=1, cents=20)} in some_money?")
    print(Money(dollars=1, cents=20) in some_money)

    print(f"{Money(dollars=55, cents=20)} in some_money?")
    print(Money(dollars=55, cents=20) in some_money)

    other_money = [
        Money(dollars=10000, cents=20),
        Money(dollars=1000, cents=20),
        Money(dollars=100, cents=20),
        Money(dollars=10, cents=20),
        Money(dollars=1, cents=20),
    ]
    print('Does list "some_money" existing in list "other_money"?')
    print(comprare_money_list(some_money, other_money))


if __name__ == '__main__':
    run_example()
