correct_username = "tanvir"
correct_password = "rahman"
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print(f"Incorrect username or password. You have {max_attempts - attempts} attempts left.")
        else:
            print("denied.")
