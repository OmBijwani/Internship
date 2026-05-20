#Question 2:
def math_operation(operation, num1, num2):
    result = 0
    if operation == "Add":
        result = num1 + num2
            
    elif operation == "Subtract":
        result = num1 - num2
        
    elif operation == "Multiply":
        result = num1 * num2

    elif operation == "Divide":
        if num2 == 0:
            print("Denominator cannot be zero")
            return
        else:
            result = num1 / num2
            
    else:
        print("Please select valid operation")
    print(result)
    

print("""
      Available operations:
      Add
      Subtract
      Multiply
      Divide""")
operation = input("Enter operation: ")
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
math_operation(operation, num1, num2)