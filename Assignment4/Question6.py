def check(num, max, min):
    if max <= min:
        print("Enter valid range")
    else:
        if num <= max and num >= min:
            print("Given number is in range")
        else:
            print("Given number is not in range")

num = int(input("Enter number: "))
max = int(input("Enter max: "))
min = int(input("Enter min: "))
check(num, max, min)