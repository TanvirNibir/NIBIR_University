import random
number_to_guess = random.randint(1, 100)
guess = None
while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number_to_guess:
        print("You got it right!")
    elif guess < number_to_guess:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")
        break