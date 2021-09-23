lucky_numbers = [4,5,75,1,2]
friends = ["Kevin", "Bob", "Don", "Atel", "Kara", "Kevin"]

friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(2, "James")
friends.remove("Kevin")
# friends.clear()
popped = friends.pop()
print(f"Popped: {popped}")

print(friends.index("Bob"))
print(friends.count("Jim"))

str_friends = [str(friend) for friend in friends]
str_friends.sort()
print(str_friends)

print(friends)
