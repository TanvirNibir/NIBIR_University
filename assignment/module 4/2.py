INCH_TO_CM = 2.54
while True:

    inches = float(input("Enter a value in inches (neg to quit): "))


    if inches < 0:
        print("Negative value exiting the program.")
        break


    cm = inches * INCH_TO_CM


    print(f"{inches} inches is equal to {cm:.2f} cm.")
