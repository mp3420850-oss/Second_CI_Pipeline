
def most_frequent(numbers):
    if not numbers:
        return None

    return max(numbers, key=numbers.count)


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers: ").split()))
    print("Most frequent element:", most_frequent(numbers))
