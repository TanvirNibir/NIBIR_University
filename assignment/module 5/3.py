number = int(input("Enter an numb: "))

if number > 1:
    for num in range(2, number):
        if number % num == 0:
            print(f"{number} is not a prime num.")
            break
    else:
        print(f"{number} is a prime num.")
else:
    print(f"{number} is not a prime num.")
