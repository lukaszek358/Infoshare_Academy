# Zadanie nr 4
#
# Zaimplementuj metodę __eq__ dla klasy Product, OrderElement oraz Order:
# * dwa produkty są równe jeżeli mają taką samą nazwę, kategorię i cenę jednostkową
# * dwie pozycje w zamówieniu są równe jeżeli ilość jest równa oraz ich produkty są równe
# * dwa zamówienia są równe jeżeli:
# - złożone przez tego samego klienta,
# - mają taką samą liczbę pozycji i są one sobie równe (nie muszą znajdować się na tych samych miejscach na liście)

import random
class Product:
    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name
                and
                self.category_name == other.category_name
                and
                self.unit_price == other.unit_price)

    def __str__(self):
        return f'Nazwa: {self.name}  |  Kategoria: {self.category_name}  |  Cena: {self.unit_price} PLN/szt.'

class OrderElement:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calc_element_price(self):
        return self.product.unit_price * self.quantity

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return  NotImplemented
        return (self.product == other.product
                and
                self.quantity == other.quantity)
    def __str__(self):
        return f'{self.product} x {self.quantity}'

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

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if len(self.order_elements) != len(other.order_elements):
            return False
        if self.client_first_name != other.client_first_name or self.client_last_name != other.client_last_name:
            return False
        for order_element in self.order_elements:
            if order_element not in other.order_elements:
                return False
            return True

    def __str__(self):
        mark_line = '--' * 30
        order_details = f'Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}'
        order_value = f'Wartość zamówienia: {self.total_price} PLN'
        ordered_product = f'Produkty zamówione: \n'
        for element in self.order_elements:
            # ordered_product = ordered_product + '\t'
            # ordered_product = ordered_product + str(element)
            # ordered_product = ordered_product + '\n'
            ordered_product = ordered_product + f'\t{element}\n'
        result = '\n'. join([mark_line, order_details, order_value, ordered_product, mark_line])
        return result

    def __len__(self):
        return len(self.order_elements)

def run_homework():
    cookie = Product(name='Ciastko', category_name= 'Jedzenie', unit_price= 4)
    # other_cookie = Product(name='Inne ciastko', category_name='Jedzenie', unit_price=4)
    juice = Product(name= 'Sok', category_name= 'Napoje', unit_price= 3)
    first_order_elements = [
        OrderElement(product= juice, quantity= 4),
        # OrderElement(product= other_cookie, quantity= 3),
        OrderElement(product= cookie, quantity= 3)
    ]

    # first_order_elements[0].quantity = 10

    second_order_elements = [
        OrderElement(product=juice, quantity=4),
        OrderElement(product=cookie, quantity=3)
        ]

    first_order = Order(client_first_name= 'Jakub', client_last_name= 'Kowalski', order_elements= first_order_elements)
    second_order = Order(client_first_name= 'Jakub', client_last_name= 'Kowalski', order_elements= second_order_elements)
    # second_order.client_last_name = 'Lewandowski'
    if first_order == second_order:
        print(f'Zamówienia są takie same.')
    else:
        print(f'Zamówienia są różne!')

if __name__ == '__main__':
    run_homework()