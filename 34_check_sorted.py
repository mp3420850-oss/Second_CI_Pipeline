
def is_sorted(numbers):
    return all(numbers[i] <= numbers[i + 1]
               for i in range(len(numbers) - 1))


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers: ").split()))
    if is_sorted(numbers):
        print("List is sorted")
    else:
        print("List is not sorted")
