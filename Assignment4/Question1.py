def max(a, b, c):
    max = 0
    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    elif c > a and c > b:
        max = c
    else:
        print("All numbers are equal")
    return max

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
max = max(a, b, c)
print("Maximum number is:", max)