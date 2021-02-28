al = [x for x in range(101) if x % 3 == 0]
bl = [x for x in range(101) if x % 5 == 0]
while True:
    try:
        a = int(input("Enter a number in range (1, 100): "))
        if a <= 0 or a > 100:
            print('You entered a wrong number')
            continue
        else:
            break
    except ValueError:
        print("AM I A JOKE TO YOU?!")
if a in al and a in bl:
    print('FizzBuzz')
else:
    if a in al:
        print("Fizz")
    elif a in bl:
        print("Buzz")
    else:
        print()