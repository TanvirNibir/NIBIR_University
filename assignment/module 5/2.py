numbers = []

while True:
    user_input = input("Enter a number or type done to quit : ")
    if user_input.lower() == "done":
        break
    numbers.append(int(user_input))
numbers.sort(reverse=True)
top_five_numbers = numbers[:5]

print("The five greatest numbers are:", top_five_numbers)

