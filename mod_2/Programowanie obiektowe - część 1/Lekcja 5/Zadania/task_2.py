# ZADANIE NR 2
# Zaimplementuj metodę __repr__ dla klas Apple oraz Potato

class Apple:
    def __init__(self, apple_name, apple_size, apple_price):
        self.apple_name = apple_name
        self.apple_size = apple_size
        self.apple_price = apple_price

    def calc_total_price(self, quantity):
        return quantity * self.apple_price
    def __repr__(self):
        return f'<Apple name = {self.apple_name}, size = {self.apple_size}, price = {self.apple_price}>'


class Potato:
    def __init__(self, potato_name, potato_size, potato_price):
        self.potato_name = potato_name
        self.potato_size = potato_size
        self.potato_price = potato_price

    def calc_total_price(self, quantity):
        return quantity * self.potato_price

    def __repr__(self):
        return f'<Potato name = {self.potato_name}, size = {self.potato_size}, price = {self.potato_price}>'

def run_task():
    green_apple = Apple(apple_name='Jabłko zielone', apple_size='XL', apple_price=5.5)
    red_apple = Apple(apple_name='Jabłko czerwone', apple_size='M', apple_price=3.25)
    batat = Potato(potato_name='Batat', potato_size='L', potato_price=7.3)

    print(green_apple)
    print(red_apple)
    print(batat)

if __name__ == '__main__':
    run_task()