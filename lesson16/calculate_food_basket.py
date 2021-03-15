def calculate_food_basket(food_basket : dict, exchange_rate : float) -> float:
    sum1 = sum(food_basket.values())
    sum2 = sum1 * exchange_rate
    return sum2
basket_example = {
'bread' : 1.1,
'milk' : 5.5
}
print(calculate_food_basket(basket_example, 2.0))