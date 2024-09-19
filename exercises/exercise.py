# lots_in_gram = 13.3
# pounds_in_talent = 20
# lots_per_pound = 32
#
# talents = float(input("Enter talents: "))
# pounds = float(input("Enter pounds: "))
# lots = float(input("Enter lots: "))
# total_lots = (talents * pounds_in_talent * lots_per_pound ) + (pounds * lots_per_pound ) + lots
# total_grams = total_lots * lots_in_gram
#
#
# kilograms = int(total_grams // 1000)
# grams = total_grams % 1000
# print(f"The weight in modern units: {kilograms} kilograms and {grams:.2f} grams.")
#size_zander = int(input("Enter the size of zender in cm : "))
# if size_zander >= 42 :
#     print("fish released successfully")
# else:
#     print("fish released unsuccessfully")
#     print(f"The fish is {size_zander:.2f} centimeters below the size limit")

# def greet():
#     print("Hello!")
#     return
#
# print("A new day starts with a greeting.")
# greet()
# print("Now we can move to other business.")
# movies = []
# movies.append((input("Enter a movie name 1 : ")))
# movies.append((input("Enter a movie name 2 : ")))
# movies.append((input("Enter a movie name 3 : ")))
# print(movie

# import random
#
# random_num = random.randint(1, 10 )
# while True:
#     guess= int(input("Guess a number between 1 and 10 "))
#     if guess > random_num:
#         print("too high")
#     elif guess < random_num:
#         print("too low ")
#     else:
#         print("you guessed it right")
#         break
print("welcome to leap year testing code ")
year = int(input("enter the year to test leap year: "))
if  year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print("leap year ")

else:
    print("not leap year")
