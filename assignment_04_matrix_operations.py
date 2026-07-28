# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(rows, cols):
    """Reads a matrix from the user."""
    matrix = []

    for i in range(rows):
        while True:
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))

            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Please enter exactly {cols} numbers.")

    return matrix


def display_matrix(matrix):
    """Displays a matrix in a neat grid."""
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()


def transpose_matrix(matrix):
    """Returns the transpose of a matrix."""
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose


def add_matrices(matrix1, matrix2):
    """Returns the sum of two matrices."""
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


def multiply_matrices(matrixA, matrixB):
    """Returns the product of two matrices."""
    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    colsB = len(matrixB[0])

    result = []

    for i in range(rowsA):
        row = []
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += matrixA[i][k] * matrixB[k][j]
            row.append(total)
        result.append(row)

    return result


def main():

    # ==============================
    # PART A - Transpose
    # ==============================
    print("PART A - Transpose Matrix")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    print("\nTransposed Matrix:")
    transpose = transpose_matrix(matrix)
    display_matrix(transpose)

    # ==============================
    # PART B - Matrix Addition
    # ==============================
    print("\nPART B - Matrix Addition")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter Matrix 1")
    matrix1 = read_matrix(rows, cols)

    print("Enter Matrix 2")
    matrix2 = read_matrix(rows, cols)

    result = add_matrices(matrix1, matrix2)

    print("\nSum of Matrices:")
    display_matrix(result)

    # ==============================
    # PART C - Matrix Multiplication
    # ==============================
    print("\nPART C - Matrix Multiplication")

    rowsA = int(input("Enter rows for Matrix A: "))
    colsA = int(input("Enter columns for Matrix A: "))

    print("Enter Matrix A")
    matrixA = read_matrix(rowsA, colsA)

    rowsB = int(input("Enter rows for Matrix B: "))
    colsB = int(input("Enter columns for Matrix B: "))

    while colsA != rowsB:
        print("\nMatrix multiplication not possible.")
        print("Columns of Matrix A must equal rows of Matrix B.")

        rowsB = int(input("Enter rows for Matrix B: "))
        colsB = int(input("Enter columns for Matrix B: "))

    print("Enter Matrix B")
    matrixB = read_matrix(rowsB, colsB)

    product = multiply_matrices(matrixA, matrixB)

    print("\nProduct of Matrices:")
    display_matrix(product)


if __name__ == "__main__":
    main()