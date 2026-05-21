def multiply(l):
    result = 1
    for i in l:
        result = result * i
    return result

l = [1, 2, 3, 4]
result = multiply(l)
print(result)