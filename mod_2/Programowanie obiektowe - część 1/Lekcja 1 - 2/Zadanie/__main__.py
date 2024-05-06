# ZADANIE. Klasy i obiekty

# Utwórz klasy do reprezentacji Produktu, Zamówienia, Jabłek i Ziemniaków.
# Stwórz po kilka obiektów typu jabłko i ziemniak i wypisz ich typ za pomocą funkcji wbudowanej type.
# Stwórz listę zawierającą 5 zamówień oraz słownik, w którym kluczami będą nazwy produktów, a wartościami instancje klasy produkt.

class Product:
    pass

class Order:
    pass

class Apple:
    pass

class Potato:
    pass

if __name__ == '__main__':

    purple_potato = Potato()
    batat = Potato()
    brown_potato = Potato()
    sweet_potato = Potato()

    red_apple = Apple()
    green_apple = Apple()
    yellow_apple = Apple()

    order_list = [Order(), Order(), Order(), Order(), Order()]

    products = {
        "Apple": Product(),
        "Tomato": Product(),
        "Potato": Product(),
        "Ananas": Product(),
        "Egg": Product(),
        "Butter": Product(),
    }

    print('purple_potato: ', type(purple_potato))
    print('batat: ', type(batat))
    print('brown_potato: ', type(brown_potato))
    print('sweet_potato: ', type(sweet_potato))
    print()
    print('yellow_apple: ', type(yellow_apple))
    print()
    print('Typ zamówienia nr 1: ', type(order_list[0]))
    print()
    for item, product in products.items():
        print('Produkt: ',item,'\t','Typ produktu: ',type(product))
        print()
    print(products)