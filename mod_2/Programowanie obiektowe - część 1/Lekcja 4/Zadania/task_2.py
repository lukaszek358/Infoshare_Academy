# Zadanie nr 2
# Napisz metodę obliczającą łączną cenę jabłek dla konkretnego obiektu Apple.
# Napisz metodę obliczającą łączną cenę ziemniaków dla konkretnego obiektu Potato.
# Wszystko ma być obliczone na podstawie podanej w argumencie informacji o liczbie kilogramów.

class Apple:
    def __init__(self, apple_name, apple_size, apple_price):
        self.apple_name = apple_name
        self.apple_size = apple_size
        self.apple_price = apple_price

    def calc_total_price(self, quantity):
        return quantity * self.apple_price

class Potato:
    def __init__(self, potato_name, potato_size, potato_price):
        self.potato_name = potato_name
        self.potato_size = potato_size
        self.potato_price = potato_price

    def calc_total_price(self, quantity):
        return quantity * self.potato_price


green_apple = Apple(apple_name= 'Jabłko zielone', apple_size= 'XL', apple_price= 5.5)
red_apple = Apple(apple_name= 'Jabłko czerwone', apple_size= 'M', apple_price= 3.25)
batat = Potato(potato_name= 'Batat', potato_size= 'L' ,potato_price= 7.3)

print(f'Cena za 10 kilogramów "{green_apple.apple_name}" wynosi {green_apple.calc_total_price(10):.2f} PLN \n')
print(f'Cena za 7,5 kilograma "{red_apple.apple_name}" wynosi {red_apple.calc_total_price(7.5):.2f} PLN \n')
print(f'Cena za 6 kilogramów "{batat.potato_name}" wynosi {batat.calc_total_price(6):.2f} PLN')