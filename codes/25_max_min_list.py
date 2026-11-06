def find_max_min(numbers):

    if not numbers:
        raise ValueError("List cannot be empty")

    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:

        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

    return maximum, minimum
