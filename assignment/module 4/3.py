smallest = None
largest = None
user_input = input("Enter a number or press Enter to quit: ")
while user_input != "":
    number = float(user_input)
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number
    user_input = input("Enter a number (or press Enter to quit): ")
if smallest is not None and largest is not None:
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
else:
    print("No numbers were entered.")
