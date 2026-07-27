# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def show_menu():
    print()
    print("=" * 28)
    print("     SIMPLE CALCULATOR")
    print("=" * 28)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
   
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def power(a, b):
    return a ** b


def read_number(message):
   
    text = input(message)
    try:
        return float(text)
    except ValueError:
        print(f'Error: "{text}" is not a number.')
        return None


def format_number(number):
    """Print 10 instead of 10.0, but leave 3.33 alone."""
    if number == int(number):
        return str(int(number))
    return str(number)


def main():
    while True:
        show_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please enter a number from 1 to 7.")
            continue

        first = read_number("Enter first number : ")
        if first == None:
            continue

        second = read_number("Enter second number: ")
        if second == None:
            continue

        if choice == "1":
            symbol = "+"
            result = add(first, second)
        elif choice == "2":
            symbol = "-"
            result = subtract(first, second)
        elif choice == "3":
            symbol = "*"
            result = multiply(first, second)
        elif choice == "4":
            symbol = "/"
            result = divide(first, second)
        elif choice == "5":
            symbol = "%"
            result = modulus(first, second)
        else:
            symbol = "**"
            result = power(first, second)

        if result == None:
            print("Error: Cannot divide by zero.")
        else:
            a = format_number(first)
            b = format_number(second)
            answer = format_number(result)
            print(f"Result: {a} {symbol} {b} = {answer}")


main()
