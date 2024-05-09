# # ZADANIE 1. DODAJ KONSTRUKTOR PRZYJMUJĄCY ODPOWIEDNIE ARGUMENTY DO KLAS: Product, Order, Apple, Potato:
# #     * Product: nazwa, nazwa kategorii, cena jednostkowa
# #     * Order: imię i nazwisko zamawiającego, lista produktów (domyślnie pusta), łączna cena (obliczona w konstruktorze jako suma cen jednostkowych z listy produktów)
# #     * Apple: nazwa gatunku, rozmiar, cena za kg
# #     * Potato: nazwa gatunku, rozmiar, cena za kg
# #
# # Utwórz kilka obiektów każdej klasy.
#
# class Product:
#     def __init__(self, name, category_name, unit_price):
#         self.name = name
#         self.category_name = category_name
#         self.unit_price = unit_price
#
# class Apple:
#     def __init__(self, apple_name, apple_size, apple_price):
#         self.apple_name = apple_name
#         self.apple_size = apple_size
#         self.apple_price = apple_price
#
# class Potato:
#     def __init__(self, potato_name, potato_size, potato_price):
#         self.potato_name = potato_name
#         self.potato_size = potato_size
#         self.potato_price = potato_price
#
# class Order:
#     def __init__(self, client_first_name, client_last_name, product_list = None):
#         self.client_first_name = client_first_name
#         self.client_last_name = client_last_name
#         if product_list is None:
#             product_list = []
#         self.product_list = product_list
#         total_price = 0
#         for product in product_list:
#             total_price = total_price + product.unit_price
#         self.total_price = total_price
#
# def run_example():
#     green_apple = Apple(apple_name= 'Green', apple_size= 'M', apple_price= 3.5)
#     red_apple = Apple(apple_name= 'Red', apple_size= 'S', apple_price= 5.5)
#     print(green_apple.apple_name, green_apple)
#     print(red_apple.apple_name, red_apple)
#
#     batat_potato = Potato(potato_name= 'Batat', potato_size= 'S', potato_price= 1.55)
#     print(batat_potato.potato_name, batat_potato)
#
#     eggs = Product(name= 'Eggs', category_name= 'Food', unit_price= 4)
#     empty_order = Order(client_first_name= 'Mikołaj', client_last_name= 'Lewandowski')
#     order = Order(client_first_name= 'Mikołaj', client_last_name= 'Lewandowski', product_list= [eggs])
#     print(eggs)
#     print(empty_order)
#     print(order)
#
# if __name__ == '__main__':
#     run_example()