# cook your dish here
for _ in range(int(input())):
    args = input().split(' ')
    number = args[0]
    to_avoid = args[1]
    to_avoid_index = number.find(to_avoid)
    
    if to_avoid_index == -1:
        print('0')
        continue
    
    new_number = list(number)
    
    carry = True
    i = to_avoid_index
    while i >= 0 and carry:
        if new_number[i] == '9':
            new_number[i] = '0'
            carry = True
        else:
            new_number[i] = str(int(new_number[i]) + 1)
            carry = False
        i -= 1
    
    i = to_avoid_index + 1
    while i < len(new_number):
        new_number[i] = '1' if to_avoid == '0' else '0'
        i += 1
        
    
    if carry:
        print(str(int("1" + "".join(new_number)) - int(number)))
    else:
        print(str(int("".join(new_number)) - int(number)))