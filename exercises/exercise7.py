
print("***** Multiplication table from 15 to 20 *****")

for i in range(15,21): # Range 15 to 21, because 20 is inculded 
    print(f"***** Multiplication table : {i} *****")
    for j in range(1,11):
        print(f"{i} x {j} = { i*j }")

    print("------------------------------------")
    print() # adding an empty line