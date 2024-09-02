print("Welcome to leap year testing code")

year = int(input("Enter a year: "))

if (year % 400 == 0):
    print("It's a Leap Year")
elif (year % 100 == 0):
    print("It's not a Leap Year")
elif (year % 4 == 0):
    print("It's a Leap Year")
else:
    print("It's not a Leap Year")

print("Thanks for your support")
