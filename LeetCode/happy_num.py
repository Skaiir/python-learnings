def isHappy(n):
    numset = {n}
    while True:
        n = sum([int(x) ** 2 for x in str(n)])
        if n == 1:
            return True
        if n in numset:
            return False
        numset.add(n)

print(bin(81))
print(bin(243))
isHappy(2)
isHappy(19)
