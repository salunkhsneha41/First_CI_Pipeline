def set_intersection(first, second):
    result = set()

    for item in first:
        if item in second:
            result.add(item)

    return result


if __name__ == "__main__":
    first = {1, 2, 3}
    second = {2, 3, 4}

    print(set_intersection(first, second))