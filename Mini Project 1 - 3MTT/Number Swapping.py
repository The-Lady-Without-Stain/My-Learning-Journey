try:
    First_number = int(input("Enter your first number: "))
    Second_number = int(input("Enter yur second number: "))

    print("\nBefore swapping:")
    print(f"First number is: {First_number}")
    print(f"Second number is: {Second_number}")

    First_number, Second_number = Second_number, First_number

    print("\nAfter swapping:")
    print(f"First number is: {First_number}")
    print(f"Second number is: {Second_number}")

except ValueError:
    print("\nInvalid input! Please, kindly enter numeric values only.")