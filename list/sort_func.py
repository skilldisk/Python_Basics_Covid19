num = [10, 25, 263, 0, 1, 72]

print("###### Before sorting #########")
print(num)

num.sort() # sort in asc order
print("###### After sorting with default reverse = False #########")
print(num)


num.sort(reverse=True) # sort in dec order
print("###### After sorting with reverese = True #########")
print(num)