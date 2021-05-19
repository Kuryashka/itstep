
def beautiful_list_generator(lst : list, marker : str, file_name : str) -> bool:
    with open(file_name, 'w+', encoding=str(marker)) as f:
        for i in lst:
            f.write(str('%s\n' % i))
            print(i)
    return True




if __name__ == '__main__':
    lll = ['batman', 'wonder woman', 'joker']
    beautiful_list_generator(lll, 'utf-8', 'superheroes.txt')
