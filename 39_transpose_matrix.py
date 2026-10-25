
def transpose_matrix(matrix):
    if not matrix:
        return []

    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    matrix = []

    for i in range(rows):
        row = list(map(int, input("Enter row: ").split()))
        matrix.append(row)

    print("Transposed Matrix:")
    for row in transpose_matrix(matrix):
        print(row)
