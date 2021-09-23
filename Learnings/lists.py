friends = ["Kevin", "John", "James"]

for friend in friends:
    print(f"Friend: '{friend}'")

#indexing
print(friends[2])
print(friends[-2])

#slicing
print(friends[1:])
print(friends[:2])

#changing elements
friends[1] = "Johnny"
print(friends[1])
