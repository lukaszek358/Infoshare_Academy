# LEKCJA 6 - ZADANIE 3

def calculate_investment_value(initial_value, percentage, years):
    result = initial_value * (1 + percentage/100) ** years
    return  result