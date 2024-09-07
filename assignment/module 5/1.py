num_dice = int(input("How many dice do you want to roll? "))
sum_of_rolls = 0
for d in range(num_dice):
    sum_of_rolls += int(input(f"Enter the result of dice {d+1}: "))
print(f"The sum of the dice is: {sum_of_rolls}")
