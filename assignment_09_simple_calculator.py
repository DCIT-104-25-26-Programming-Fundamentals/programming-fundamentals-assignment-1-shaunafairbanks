
# Functions for arithmetic operations

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def exponentiation(a, b):
    return a ** b


def display_menu():
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    while True:
        display_menu()

        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please select a number between 1 and 7.")
            continue

        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = addition(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")

        elif choice == "2":
            result = subtraction(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")

        elif choice == "3":
            result = multiplication(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")

        elif choice == "4":
            result = division(num1, num2)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {num1} / {num2} = {result}")

        elif choice == "5":
            result = modulus(num1, num2)
            if result is None:
                print("Error: Cannot perform modulus by zero.")
            else:
                print(f"Result: {num1} % {num2} = {result}")

        elif choice == "6":
            result = exponentiation(num1, num2)
            print(f"Result: {num1} ** {num2} = {result}")


# Start the program
if __name__ == "__main__":
    main()