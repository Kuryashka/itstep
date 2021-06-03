import json
from multiprocessing import Process


def greater_then_zero(path : str):
    with open(path, 'rb') as f:
        element = f.read()
        elements = json.loads(element.decode("utf-8"))
        result = ''
        for i in elements:
            if elements.get(i) > 0:
                result += str(elements.get(i)) + '\n'
        with open("greater.txt", "wb") as f:
            f.write(result.encode('utf-8'))

def lower_then_zero(path : str):
    with open(path, 'rb') as f:
        element = f.read()
        elements = json.loads(element.decode("utf-8"))
        result = ''
        for i in elements:
            if elements.get(i) < 0:
                result += str(elements.get(i)) + '\n'
        with open("lower.txt", "wb") as f:
            f.write(result.encode('utf-8'))


if __name__ == '__main__':
    n = input("Enter the way to a file in proper way(json):\n")
    t1 = Process(target=lower_then_zero(n))
    t1.start()
    t2 = Process(target=greater_then_zero(n))
    t2.start()
