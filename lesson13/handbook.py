id_codes = [5555, 6666, 7777, 2345, 5675]
phone_numbers = [9654785657, 9654565657, 9654734557]


def menu():
    print("1 : sort id codes\n2 : sort phone numbers\n3 : print users with id codes and phone numbers\n4 : exit")

while True:
    menu()
    n = int(input("Choose an option: "))

    if n <= 0 or n >= 5:
        print("choose valid option") 
        continue
    elif n == 1:
        print(sorted(id_codes))
        break
    elif n == 2:
        print(sorted(phone_numbers))
        break
    elif n == 3:
        print (sorted(id_codes), (sorted(phone_numbers)))
    elif n == 4:
        break
    break
