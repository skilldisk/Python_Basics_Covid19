print("Check whether the number is Prime")

number = int(input("Enter a number:"))
prime = True

if number <= 1:
    print("Enter the number greater than 1")
else:
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    
    if prime:
        print(f'Number {number} is a prime number')
    else:
        print(f'Number {number} is not a prime number')