def roll_dice(sides):
    from time import time
    return int((time() * 1000) % sides) + 1

def main():
    sides = int(input("Enter the number of sides on the dice: "))
    result = 0
    while result != sides:
        result = roll_dice(sides)
        print(result)

if __name__ == "__main__":
    main()
