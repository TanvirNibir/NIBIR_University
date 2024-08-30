print("Therse is 4 types of cabbin in this cruise LUX, A, B, C ")

class_cabin_cruise = input("Enter the class cabin cruise name you want to stay : ")
if class_cabin_cruise == "LUX":
    print(" it's upper-deck cabin with a balcony.")
elif class_cabin_cruise == "A":
    print(" it's above the car deck, equipped with a window.")
elif class_cabin_cruise == "B":
    print("it's windowless cabin above the car deck.")

elif class_cabin_cruise == "C":
    print("it's windowless cabin below the car deck.")

else:
    print("Invalid cabin class.!")