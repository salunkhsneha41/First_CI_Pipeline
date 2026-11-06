def is_anagram(first, second):
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()

    if len(first) != len(second):
        return False

    for char in first:
        if first.count(char) != second.count(char):
            return False

    return True


if __name__ == "__main__":
    first = input("Enter first string: ")
    second = input("Enter second string: ")

    if is_anagram(first, second):
        print("Strings are Anagrams")
    else:
        print("Strings are not Anagrams")