print("Welcome to Homoglobin value test centre for Adults! ")
print(" choose your gender 1 = Female, 2 = male ")
Gender = int(input("What's gender? "))
level= int(input("what is the value of your Homoglobin in g/l? "))
if Gender == 1:
    if 117 <= level <=155:
        print("Your Homoglobin level is normal ")

    elif  117 > level :
        print("Your Homoglobin level is Low ")

    else: #level > 155:
        print("Your Homoglobin level is High ")

elif Gender == 2 :
    if 134 <= level <= 167:
        print("Your Homoglobin level is Normal ")

    elif 134 > level:
        print("Your Homoglobin level is Low ")
    else:
        print("Your Homoglobin level is High ")
else:
        print("please choose currect gender ")



