try:
    number = int(input("Enter a number besides zero: "))
    1 / number
    print(f"Your number is {number}")
except ZeroDivisionError:
    print("Don't enter a zero")
except ValueError as err:
    print(f"Invalid input: {err}")

