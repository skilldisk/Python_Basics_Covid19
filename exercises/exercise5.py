std_code = "11 Delhi, 22 Mumbai, 33 Kolkata, 44 Chennai, 40 Hyderabad, 80 Bangalore, 20 Pune, 79 Ahmedabad"

# Convert the string to list, splitting at ','
std_code_list = std_code.split(",")

std_code_dict = {}  # Create a empty dictionary
for data in std_code_list:
    data.strip()
    list_data = data.split()
    std_code_dict[list_data[1]] = int(
        list_data[0]
    )  # add city name as key and std code as data

# print the dictionay
print(std_code_dict)

