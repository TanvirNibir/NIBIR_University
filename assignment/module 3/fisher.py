size_zander = int(input("Enter the size of zender in cm : "))
if size_zander >= 42 :
    print("fish released successfully")
else:
    below = 42 - size_zander
    print("fish released unsuccessfully")
    print(f"The fish is {below:.2f} centimeters below the size limit")


