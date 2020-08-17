print("Find the sum of digits in a Number")
number = int(input("Enter a number: "))
n = number
result = 0
remainder = 0

while number!= 0:
    remainder = number % 10
    result = result + remainder
    number = int(number/10)

print(f"The sum of digits in {n} = {result}")