while True:
    try:
        a = int(input('Enter a number: '))
        break
    except ValueError:
        print("you entered a wrong number")
if a % 2 == 0 and a != 0:
    print('The number is even')
elif a == 0:
    print("You entered zero")
else:
    print("the number is odd")