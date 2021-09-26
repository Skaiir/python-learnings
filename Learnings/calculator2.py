number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))
operator = input("Enter char: ")

result = None

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
elif operator == "^":
    result = number1 ** number2
else:
    result = "Something is wrong"

print(result)