def roll_dice():
    return 1

def main():
    result = 0
    while result != 6:
        result = roll_dice()
        print(result)

if __name__ == "__main__":
    main()
