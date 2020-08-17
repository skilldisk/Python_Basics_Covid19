
def students_data(name, email = None, **kwargs):
    # print(kwargs)

    print(f'name : {name}')
    print(f'email : {email}')

    for key in kwargs:
        print(f'{key} : {kwargs[key]} ')


students_data('Skill Disk',email='info@skilldisk.com')




# # def addition(x, *args):

# #     for i in args:
# #         x += i
    
# #     print(f'addition of all the numbers  is {x} ')


# # a = addition

# # a(2,20)



# def add_with_data(a, b, x=0, y=0, **kwargs):
#     print(f'a={a}, b={b}, x={x} and y={y}: result = {a+b+x+y}')
#     print(kwargs)

# add_with_data(5, 15, 1, 2) # position assignment

# add_with_data(2, 3, y=3, c=10, name="skill disk") # keyword assignment