even = [0, 2, 4, 6, 8, 10, 12]

print("###### Before using POP #########")
print(even)

# Pop will remove the last data
even.pop() # default index is -1
print("###### After using POP on the list even #########")
print(even)


# can remove the data by specifyi8ng index value also
even.pop(1) 
print("###### After specifying index value 1 to the pop method #########")
print(even)