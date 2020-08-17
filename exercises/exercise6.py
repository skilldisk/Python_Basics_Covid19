print("****** Printig Even Numbers ******")
n1 = int(input("Enter the starting number :"))
n2 = int(input("Enter the ending number :"))

# If starting number is Odd number change it to even number by adding 1
if n1 % 2 == 1:
    n1 += 1


for i in range(n1,n2,2):
    print(i)