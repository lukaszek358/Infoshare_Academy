# Zadanie 3
# Napisz nową klasę 'OrderElement', która będzie reprezentować pozycję w zamówieniu.
# Taka pozycja będzie zawierać informacje o produkcie i liczbie jego sztuk w zamówieniu.
# W klasie 'OrderElement' zaimplementuj metodę wypisującą (info o liczbie elementów i produkcie)
# W klasie 'OrderElement' zaimplementuj metodę obliczającą cenę danej pozycji w zamówieniu.
# W klasie 'Order' zastąp listę produktów listą pozycji w zamówieniu (zmodyfikuj funkcje, np. generowanie zamówienia).
# Napisz metodę obliczającą łączną wartość zamówienia - suma wartości wszystkich pozycji
# (wykorzystując napisaną metodę z klasy 'OrderElement')
# Wykorzystaj ją w konstruktorze do inicjalizacji łącznej wartości zamówienia.

import random
class Product:
    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price

    def print_self_product(self):
        print(f'Nazwa: {self.name}  |  Kategoria: {self.category_name}  |  Cena: {self.unit_price} PLN/szt.')

class OrderElement:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calc_element_price(self):
        return self.product.unit_price * self.quantity

    def print_self(self):
        self.product.print_self_product()
        print(f'\t\t x {self.quantity}')

class Order:
    def __init__(self, client_first_name, client_last_name, order_elements = None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if order_elements is None:
            order_elements= []
        self.order_elements = order_elements
        self.total_price = self.calc_total_price()

    def calc_total_price(self):
        total_price = 0
        for element in self.order_elements:
            total_price = total_price + element.calc_element_price()
        return total_price

    def print_self(self):
        print('--' * 30)
        print(f'Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}')
        print(f'Wartość zamówienia: {self.total_price} PLN')
        print('Produkty zamówione:')
        for element in self.order_elements:
            print('\t', end= '')
            element.print_self()
        print('--' * 30)
        print()

def generate_order():
    number_of_products = random.randint(1, 15)
    order_elements_list = []
    for product_number in range(number_of_products):
        product_name = f'Produkt_{product_number + 1}'
        category_name = 'Inne'
        unit_price = random.randint(1, 30)
        product = Product(product_name, category_name, unit_price)
        quantity = random.randint(1, 20)
        order_elements_list.append(OrderElement(product, quantity))

    order = Order(client_first_name= 'Mikołaj' ,client_last_name= 'Lewandowski', order_elements= order_elements_list)
    return order
def run_homework():
    first_order = generate_order()
    first_order.print_self()
    second_order = generate_order()
    second_order.print_self()

if __name__ == '__main__':
    run_homework()