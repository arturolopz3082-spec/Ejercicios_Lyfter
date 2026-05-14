while True:
    try:
        current_number = float(input("\nEnter the current number: "))
        break
    except ValueError:
        print("Error: Invalid number.")


while True:
    print("\n--- Calculator ---")
    print("Current number:", current_number)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Clear result")
    print("6. Exit")

    option = input("Select an option: ")

    if option == "6":
        print("Calculator closed.")
        break

    elif option == "5":
        current_number = 0
        print("Result cleared.")
        continue

    elif option not in ["1", "2", "3", "4"]:
        print("Error: Invalid option.")
        continue

    try:
        new_number = float(input("Enter another number: "))
    except ValueError:
        print("Error: Invalid number.")
        continue

    if option == "1":
        current_number += new_number

    elif option == "2":
        current_number -= new_number

    elif option == "3":
        current_number *= new_number

    elif option == "4":
        if new_number == 0:
            print("Error: Cannot divide by zero.")
            continue

        current_number /= new_number

    print("Result:", current_number)
