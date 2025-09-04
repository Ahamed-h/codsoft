# Simple Calculator

def calculator():
    print("=== Simple Calculator ===")

    # Get user input
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    # Perform calculation
    if choice == '1' or choice == '+':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif choice == '2' or choice == '-':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif choice == '3' or choice == '*':
        result = num1 * num2
        print(f"\nResult: {num1} × {num2} = {result}")
    elif choice == '4' or choice == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"\nResult: {num1} ÷ {num2} = {result}")
        else:
            print("\nError: Division by zero is not allowed!")
    else:
        print("\nInvalid choice! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    calculator()
