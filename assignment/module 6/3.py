def gallons_to_liters(gallons):
    return gallons * 3.78541

def main():
    while True:
        gallons = float(input("Enter the volume in gal (or a negative number to quit): "))
        if gallons < 0:
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gal is equal to {liters:.2f} liters.")

if __name__ == "__main__":
    main()
