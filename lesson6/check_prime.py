while True:
    print("prime number checker")
    number = int(input("Enter a number: "))
    if number > 1:
        z = False
        for i in range(2, number):
            if number % i == 0:
                z = True
                break
        if z:
            print(number, 'is', "not a prime number")
        else:
            print(number, 'is', "a prime number")
