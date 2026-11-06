def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Negative numbers are not allowed")

    if number == 0:
        return "0"

    binary = ""

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2

    return binary


if __name__ == "__main__":
    number = int(input("Enter a decimal number: "))
    print("Binary:", decimal_to_binary(number))