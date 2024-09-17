airports = {}

while True:
    # Asking user to choose option
    print("\nChoose an option:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    option = input("Enter the option number (1/2/3): ")

    # Option 1: Enter a new airport
    if option == "1":
        icao_code = input("Enter the ICAO code: ").upper()  # ICAO codes are usually uppercase
        airport_name = input("Enter the airport name: ")

        if icao_code in airports:
            print("This airport is already in the system.")
        else:
            airports[icao_code] = airport_name
            print(f"Airport '{airport_name}' with ICAO code '{icao_code}' has been added.")

    # Option 2: Fetch airport information
    elif option == "2":
        icao_code = input("Enter the ICAO code to fetch: ").upper()

        if icao_code in airports:
            print(f"The airport with ICAO code '{icao_code}' is {airports[icao_code]}.")
        else:
            print(f"No airport found with ICAO code '{icao_code}'.")

    # Option 3: Quit the program
    elif option == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please enter 1, 2, or 3.")