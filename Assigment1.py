#Question !:
name = input("Whats your name?: ")
Class = input("Whats your class?: ")
physics = int(input("Enter marks in Physics: "))
chemistry = int(input("Enter marks in Chemistry: "))
maths = int(input("Enter marks in Maths: "))
english = int(input("Enter marks in English: "))
hindi = int(input("Enter marks in Hindi: "))
total = physics + chemistry + maths + english + hindi
percentage = (total/500)*100
print("NAME: ",name)
print("CLASS: ",Class)
print("PERCENTAGE: ",percentage)

#Question 3:
if percentage >= 60:
    print("Grade A")
elif percentage >= 50 and percentage < 60:
    print("Grade B")
elif percentage >= 40 and percentage < 50:
    print("Grade C")
elif percentage >= 33 and percentage < 40:
    print("Grade D")
else:
    print("Fail")

#Question 2:
string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")
final = string1 + string2
print(final.lower())
print(final.upper())
print(final.title())
print(final.swapcase())
print(final.center(10))
print(final.capitalize())
print(final.casefold())
print(final.count("y"))
print(final.endswith("y"))
print(final.find("y"))
print(final.isalnum())
print(final.isdigit())
print(final.isspace())
print(final.isnumeric())
print(final.replace("e", "i"))

x = 10

print("Initial value:", x)

x += 5
print("After += :", x)

x -= 3
print("After -= :", x)

x *= 2
print("After *= :", x)

x /= 4
print("After /= :", x)

x %= 3
print("After %= :", x)

x //= 1
print("After //= :", x)

x **= 2
print("After **= :", x)