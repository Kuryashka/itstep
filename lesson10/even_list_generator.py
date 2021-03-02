def even_list_generate_(num_1, num_2):


    even_number_list = []
    for num in range(num_1, num_2 + 1):
        if num % 2 == 0 and num != 0:
            even_number_list.append(num)
    return even_number_list
print(even_list_generate_(10, 20))