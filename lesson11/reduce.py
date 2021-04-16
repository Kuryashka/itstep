from functools import reduce
int_list = [2, 8, 9, 23, 5]
result = reduce(lambda x, y: x*y, int_list)
if __name__ == '__main__':
  print(result)
