def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def main():
    numbers = [20, 30, 40, 50, 60]
    total = sum_of_list(numbers)
    print(f"The sum of the list is: {total}")

if __name__ == "__main__":
    main()
