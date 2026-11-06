def rotate_list(items, k):

    if len(items) == 0:
        return []

    n = len(items)
    k = k % n

    if k == 0:
        return items.copy()

    rotated_list = items[-k:] + items[:-k]

    return rotated_list


if __name__ == "__main__":
    items = list(map(int, input("Enter list elements: ").split()))
    k = int(input("Enter rotation position: "))

    print("Rotated list is:", rotate_list(items, k))