# Zadanie nr 1
# Zmodyfikuj rozwiązanie ostatniego zadania (poprzednia lekcja).
# Zamień funkcje wypisywania produktu i zamówienia na metody.

import random

class Product:
    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price

    def print_self_product(self):
        print(f'Nazwa: {self.name}   |   Kategoria: {self.category_name}  |   Cena: {self.unit_price} PLN/szt.')


class Order:
    def __init__(self, client_first_name, client_last_name, product_list = None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if product_list is None:
            product_list = []
        self.product_list = product_list
        total_price = 0
        for product in product_list:
            total_price = total_price + product.unit_price
        self.total_price = total_price

    def print_self(self):
        print('--' * 30)
        print(f'Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}')
        print(f'Wartość zamówienia: {self.total_price} PLN')
        print('Produkty zamówione:')
        for product in self.product_list:
            print('\t', end= '')
            product.print_self_product()
        print('--' * 30)
        print()

def generate_order():
    number_of_products = random.randint(1, 15)
    products = []
    for product_number in range(number_of_products):
        product_name = f'Produkt_{product_number + 1}'
        category_name = 'Inne'
        unit_price = random.randint(1, 30)
        product = Product(product_name, category_name, unit_price)
        products.append(product)

    order = Order(client_first_name= 'Mikołaj' ,client_last_name= 'Lewandowski', product_list= products)
    return order

def run():
    first_order = generate_order()
    first_order.print_self()
    second_order = generate_order()
    second_order.print_self()

if __name__ == '__main__':
    run()