#Question 3:
number = input("Enter number:")
reversed = number[::-1]

if number == reversed:
    print("Palindrome")
else:
    print("Not palindrome")