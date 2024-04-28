# ZDEFINIOWANE PRODUKTY W POSTACI SŁOWNIKA

products = {
    'chleb':{
        'quantity': 100,
        'price' : 3.5
    },
    'jabłka':{
        'quantity': 50,
        'price': 3.2
    }
}

# FUNKCJA AKTUALIZUJĄCA LICZBĘ DOSTĘPNYCH PRODUKTÓW
def update_products_quantity(product_name, ordered_quantity):
    products[product_name]['quantity']-= ordered_quantity


