while True:
    num_1 = (int(input("Enter first number: ")))
    arg = input("Enter one of the given mathematical actions\n '+, -, *, /'\n")
    num_2 = (int(input("Enter second number: ")))
    res = ()
    if arg == '+':
        res = num_1 + num_2
        print(res)
    elif arg == '-':
        res = num_1 - num_2
        print(res)
    elif arg == '*':
        res = num_1 * num_2
        print(res)
    elif arg == '/':
        res = float(num_1 // num_2)
        print(res)
    else:
        print("Enter valid argument for an action")
        break
''' Не понимаю почему при делении меньшего числа на большее ответ не пишется правильно, если можете, напишите, пожалуйста, в комментах к работе на майстате что не так'''