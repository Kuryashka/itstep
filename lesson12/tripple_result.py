def tripple_result(func):
    def wrapper(a, b):
        return (a + b) * 3
    return wrapper

@tripple_result
def add(a, b):
    return a + b

if __name__ == '__main__':
    print(add(5, 5))

