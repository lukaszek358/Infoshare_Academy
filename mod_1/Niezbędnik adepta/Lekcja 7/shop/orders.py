from product_store import products, update_products_quantity

orders = [
    {
        'product' : 'chleb',
        'quantity': 10,
        'total_price': 35
    }
]

def create_new_order(product_name, quantity):

    price = products[product_name]['price']
    available_quantity = products[product_name]['quantity']

    if available_quantity < quantity:
            print('Nie ma tyle towaru')
            return None

    total_price = quantity * price
    new_order = {
        'product': product_name,
        'quantity': quantity,
        'total_price': total_price
    }
    update_products_quantity(product_name, quantity)

    orders.append(new_order)
    return new_order