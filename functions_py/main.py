print("**** Functions ****")

def addition():
    """
    This is addition function
    it will not take any parameters

    SKILL DISK
    """
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))

    print(f"addition of {a} + {b} = {a+b}")



def add_with_data(x, y=0):
    print(f'the addition of x={x} and y={y} is {x+y}')


def add_data_ret(x, y, *args):
    print(args)
    return x+y



