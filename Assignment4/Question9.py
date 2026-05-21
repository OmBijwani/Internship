def count(str):
    up = 0
    low = 0
    for char in str:
        if char.isupper():
            up = up + 1
        else:
            low = low + 1
    print("Upper case:", up) 
    print("Lower case:", low) 

str = input("Enter string: ")
count(str)