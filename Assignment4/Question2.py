def distinct(l1, l2):
    new_l = []
    for i in l1:
        if i not in l2:
            new_l.append(i)
    return new_l

l1 = [1, 2, 3]
l2 = [2, 3, 4]
result = distinct(l1, l2)
print(result)