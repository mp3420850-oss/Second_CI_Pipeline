
def missing_number(numbers, n):
    result = 0

    for i in range(1, n + 1):
        result ^= i

    for num in numbers:
        result ^= num

    return result


if __name__ == "__main__":
    n = int(input("Enter total numbers (n): "))
    numbers = list(map(int, input("Enter numbers: ").split()))

    print("Missing number:", missing_number(numbers, n))
