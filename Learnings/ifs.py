is_old = False
is_male = True

if is_old:
    print("You are old")
else:
    print("You are not old")

if is_male and is_old:
    print("You are an old male")

if not is_male or not is_old:
    print("You are not a male, or you aren't old")

if True:
    pass
elif True and True:
    pass
else:
    pass

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(21, 33, 100))