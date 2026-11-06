def sum_of_list(numbers):

    total = 0

    for num in numbers:
        total = total + num

    return total


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers: ").split()))

    print("Sum of list is:", sum_of_list(numbers))