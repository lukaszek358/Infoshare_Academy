# ZADANIE 1.
# Zabezpiecz listę pozycji w zamówieniu i łączną wartość zamówienia przed utratą spójności. W tym celu:
# - zamień listę pozycji w zamówieniu na zmienną prywatną.
# - zamień również metodę obliczającą łączny koszt zamówienia na prywatną.
# - dodaj metodę (public) umożliwiającą dodanie nowego produktu do zamówienia (potrzebne informacje o produkcie i ilości).
# - pamiętaj wywołać ponownie przeliczenie łącznej wartości zamówienia.


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
        return f'Nazwa: {self.name}     |   Kategoria: {self.category_name}     |   Cena: {self.unit_price} PLN/szt.'

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
        self._order_elements = order_elements
        self.total_price = self._calc_total_price()

    def _calc_total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price = total_price + element.calc_element_price()
        return total_price

    def add_product_to_order(self, product, quantity):
        new_element = OrderElement(product, quantity)
        self._order_elements.append(new_element)
        self.total_price = self._calc_total_price()

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if len(self) != len(other):
            return False
        if self.client_first_name != other.client_first_name or self.client_last_name != other.client_last_name:
            return False
        for order_element in self._order_elements:
            if order_element not in  other.order_elements:
                return False
            return True

    def __str__(self):
        mark_line = '--' * 30
        order_details = f'Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}'
        order_value = f'Wartość zamówienia: {self.total_price} PLN'
        ordered_product = f'Produkty zamówione: \n'
        for element in self._order_elements:
            # ordered_product = ordered_product + '\t'
            # ordered_product = ordered_product + str(element)
            # ordered_product = ordered_product + '\n'
            ordered_product = ordered_product + f'\t{element}\n'
        result = '\n'. join([mark_line, order_details, order_value, ordered_product, mark_line])
        return result

    def __len__(self):
        return len(self.order_elements)

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
    print(first_order)

    cookie = Product(name = 'Ciastko', category_name= 'Jedzenie', unit_price= 4)
    first_order.add_product_to_order(product= cookie, quantity= 10)
    print(first_order)

if __name__ == '__main__':
    run_homework()