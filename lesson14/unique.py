def intersect(tup1=(1, 2, 3), tup2=(1, 3, 4), tup3=(1, 2, 3)):
    l = []
    for i in tup1:
        if i in tup1 and i not in tup2 and i not in tup3:
            l.append(i)
        if i in tup2 and i not in tup1 and i not in tup3:
            l.append(i)
        if i in tup3 and i not in tup1 and i not in tup2:
            l.append(i)
    for i in tup2:
        if i in tup1 and i not in tup2 and i not in tup3:
            l.append(i)
        if i in tup2 and i not in tup1 and i not in tup3:
            l.append(i)
        if i in tup3 and i not in tup1 and i not in tup2:
            l.append(i)
    for i in tup3:
        if i in tup1 and i not in tup2 and i not in tup3:
            l.append(i)
        if i in tup2 and i not in tup1 and i not in tup3:
            l.append(i)
        if i in tup3 and i not in tup1 and i not in tup2:
            l.append(i)
    l = tuple(l)
    return l
print(intersect((4, 2, 6, 7), (1, 2, 7, 2, 9), (2, 2, 2, 7, 1)))