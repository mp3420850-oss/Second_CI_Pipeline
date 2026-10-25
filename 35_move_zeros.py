
def move_zeros(numbers):
    non_zeros = [num for num in numbers if num != 0]
    zeros = [0] * (len(numbers) - len(non_zeros))
    return non_zeros + zeros


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers: ").split()))
    print("After moving zeros:", move_zeros(numbers))
