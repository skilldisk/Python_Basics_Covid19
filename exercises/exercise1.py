# Take the input of two numbers and perform arithematic operations on it and print the result.

# Read the input from the user
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

# addition
total = num1 + num2
print("############## Addition ##############")
print(f"Sum of {num1} + {num2} = {total}")

# Substraction
difference = num1 - num2
print("############## Substraction ##############")
print(f"Differenc of {num1} - {num2} = {difference}")

# Multiplication
product = num1 * num2
print("############## Multiplication ##############")
print(f"Product of {num1} x {num2} = {product}")

# Division
div = num1 / num2
print("############## Division ##############")
print(f"Division of {num1} / {num2} = {div}")

# Modulus
remainder = num1 % num2
print("############## Modulus ##############")
print(f"Remainder of {num1} % {num2} = {remainder}")

# Floor Division
quotient = num1 // num2
print("############## Floor Division ##############")
print(f"Quotient of {num1} // {num2} = {quotient}")

