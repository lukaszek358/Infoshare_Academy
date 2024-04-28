# Zadanie nr 3
#
# Zmodyfikuj rozwiązanie zadania pierwszego.
# Zamykając logikę w pliku main w funkcję, która wywoła się, gdy skrypt ten zostanie bezpośrednio uruchomiony __name__ → __main__.

from orders import create_new_order
from product_store import products

def run_shop():
    print('Witaj w naszym sklepie!')

    product_name = input(f'Jaki towar chcesz kupić:')
    quantity = int(input('Ile kilogramów/sztuk chcesz kupić?:'))

    result = create_new_order(product_name, quantity)
    if result is not None:
        total_price = result['total_price']
        print(f'Łączny koszt zakupów wynosi {total_price} PLN\n')
        print(f'Pozostało towaru:\n{products}')

if __name__ == '__main__':
    run_shop()