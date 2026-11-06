def bubble_sort(numbers):

    result = numbers.copy()
    n = len(result)

    for i in range(n):

        for j in range(0, n - i - 1):

            if result[j] > result[j + 1]:

                temp = result[j]
                result[j] = result[j + 1]
                result[j + 1] = temp

    return result


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers: ").split()))

    print("Sorted list is:", bubble_sort(numbers))