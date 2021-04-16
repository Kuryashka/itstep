def find_most_in_food_basket(food_basket: dict, max_cost = True) -> set:
    all_values = food_basket.values()
    if max_cost == True:
        max_value = max(all_values)
        return max_value
    else:
        min_value = min(all_values)
        return min_value
    
        
basket_example = {
'bread' : 1.1,
'milk' : 5.5,
'apple' : 6.7,
'bag' : 10.5,
}

if __name__ == '__main__':
    print(find_most_in_food_basket(basket_example, True))

"""Не понял, как вывести наименования объектов, а не их цену"""
