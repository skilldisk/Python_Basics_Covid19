print("******* Fibonacci Sequences *******")

nterms = int(input("how many terms ? : "))
current = 0
previous = 1
count = 0
next_term = 0
if nterms <= 0:
    print("Enter a positive number")
elif nterms == 1:
    print('0')
else:
    while count < nterms:
        print(next_term)
        current = next_term
        next_term = previous + current
        previous = current
        count += 1
        