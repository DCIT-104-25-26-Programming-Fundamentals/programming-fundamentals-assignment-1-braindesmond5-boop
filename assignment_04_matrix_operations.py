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

def read_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    for r in range(rows):
        line = input(f"Enter row {r + 1}: ")
        row = []
        for value in line.split():
            row.append(int(value))
        matrix.append(row)
    return matrix

def print_matrix(title, matrix):
    print()
    print(title)
    for row in matrix:
        for value in row:
            print(f"{value:4}", end="")
        print()

def transpose(matrix):
    result = []
    for c in range(len(matrix[0])):
        new_row = []
        for r in range(len(matrix)):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result

def add_matrices(a, b):
    result = []
    for r in range(len(a)):
        new_row = []
        for c in range(len(a[0])):
            new_row.append(a[r][c] + b[r][c])
        result.append(new_row)
    return result

def multiply_matrices(a, b):
    result = []
    for r in range(len(a)):
        new_row = []
        for c in range(len(b[0])):
            total = 0
            for k in range(len(b)):
                total = total + a[r][k] * b[k][c]
            new_row.append(total)
        result.append(new_row)
    return result

def main():
    # PART A
    print("PART A - Transpose a Matrix")
    matrix = read_matrix()
    print_matrix("Original Matrix:", matrix)
    print_matrix("Transposed Matrix:", transpose(matrix))

    # PART B
    print()
    print("PART B - Add Two Matrices")
    first = read_matrix()
    second = read_matrix()
    print_matrix("Sum:", add_matrices(first, second))

    # PART C
    print()
    print("PART C - Multiply Two Matrices")
    a = read_matrix()
    b = read_matrix()
    print_matrix("Product (A x B):", multiply_matrices(a, b))

main()
