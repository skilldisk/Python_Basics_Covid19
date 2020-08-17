
# set_temp = 30.0 # set the temp to 30 degree
# room_temp = float(input("Enter the room temperature in d c:"))

# if room_temp > set_temp :
#     print(f"Room temperature {room_temp} is greater than Set temperature {set_temp}, TURN ON THE FAN")
# else:
#     print(f"Room temperature {room_temp} is less than Set temperature {set_temp}, TURN OFF THE FAN")


marks = float(input("Enter the marks between 0 to 1: "))

if marks > 1.0 or marks < 0:
    print("Entered marks is not in the range of 0 to 1")
elif marks >= 0.7:
    print("FCD")
elif marks >=0.5:
    print('FC')
else:
    print('SC')