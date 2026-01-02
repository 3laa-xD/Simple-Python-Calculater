# Simple-Python-Calculater


operator = input("enter an operator ( + - * / ): ")


if operator == '+':
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))
    result = num1 + num2
    print(f"the result is {result}")


elif operator == '-':
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))
    result = num1 - num2
    print(f"the result is {result}")


elif operator == '*':
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))
    result = num1 * num2
    print(f"the result is {result}")


elif operator == '/':
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))
    if num2 == 0:
        print("You cannot divide by zero")
    else:
        result = num1 / num2
        print(f"the result is {result}")


else:
    print(f"the operator {operator} is invalid")
