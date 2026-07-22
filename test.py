# simple python program

def calculator():
    print("Simple Python Calculator (+ and -)")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")

    choice = input("Enter choice (1/2): ")

    if choice in ("1", "2"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return

        if choice == "1":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
    else:
        print("Invalid input. Please select a valid operation.")


if __name__ == "__main__":
    calculator()
