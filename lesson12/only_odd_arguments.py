def only_add_numbers(func):
    z = False
    def wrapper(*args):
        for i in args:
            if i % 2 == 0:
                print('Please, choose odd arguments!')
                return z
        return func(args)
    return wrapper

@only_add_numbers
def add(args):
    return sum(list(args))

print(add(5, 5))

@only_add_numbers
def multiply(args):
    m = 1
    for i in list(args):
        m *= i
    return m

print(multiply(5, 5, 5))
