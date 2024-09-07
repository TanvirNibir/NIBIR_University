def remove_odd_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]


def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_list = remove_odd_numbers(original_list)

    print("Original list:", original_list)
    print("List with odd numbers removed:", filtered_list)


if __name__ == "__main__":
    main()
