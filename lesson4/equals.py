while True:
    try:
        a = int(input("Enter the first number: "))
        break
    except ValueError:
        print("AM I A JOKE TO YOU?!")
        continue
while True:
    try:
        b = int(input("Enter the second number: "))
        break
    except ValueError:
        print("AM I A JOKE TO YOU?!")
        continue
if a == b:
    print("EQUALS")
else:
    if a > b:
        print(a, b)
    if a < b:
        print(b, a)