def is_anagram(first, second):

    first_clean = first.replace(" ", "").lower()
    second_clean = second.replace(" ", "").lower()

    if len(first_clean) != len(second_clean):
        return False

    for character in first_clean:
        if first_clean.count(character) != second_clean.count(character):
            return False

    return True


if __name__ == "__main__":
    first = input("Enter the first string: ")
    second = input("Enter the second string: ")

    print("Are they anagrams?", is_anagram(first, second))