numbers = [1, 5, 0, -1, -6, 7, -10]
filtered_numbers = filter(lambda num : num < 0, numbers)
filtered_numbers_ = list(filtered_numbers)
if __name__ == '__main__':
    print(filtered_numbers_)
