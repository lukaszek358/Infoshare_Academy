# ZADANIE NR 2
# Napisz funkcję wypisującą produkt i zamówienie.
# Podczas wypisywania zamówienia skorzystaj z wypisywania produktu.

class Product:
    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price

class Apple:
    def __init__(self, apple_name, apple_size, apple_price):
        self.apple_name = apple_name
        self.apple_size = apple_size
        self.apple_price = apple_price

class Potato:
    def __init__(self, potato_name, potato_size, potato_price):
        self.potato_name = potato_name
        self.potato_size = potato_size
        self.potato_price = potato_price

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

def print_product(product):
    print(f'Nazwa: {product.name}   |   Kategoria: {product.category_name}  |   Cena: {product.unit_price} PLN/szt.')

def print_order(order):
    print('--' * 30)                                                                                                    # ROZDZIELNIK ZAMÓWIEŃ ZBUDOWANY ZE ZNAKÓW
    print(f'Zamówienie złożone przez: {order.client_first_name} {order.client_last_name}')
    print(f'Wartość zamówienia: {order.total_price} PLN')
    print('Produkty zamówione:')
    for product in order.product_list:
        print('\t', end= '')
        print_product(product)
    print('--' * 30)
    print()

def run():
    eggs = Product(name= 'Eggs', category_name= 'Food', unit_price= 1.5)
    empty_order = Order(client_first_name= 'Mikołaj', client_last_name= 'Lewandowski')
    order = Order(client_first_name= 'Mikołaj', client_last_name= 'Lewandowski', product_list= [eggs, eggs, eggs, eggs])

    print_order(empty_order)
    print_order(order)

if __name__ == '__main__':
    run()