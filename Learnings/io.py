employee_file = open("./employees.txt", "r")

# r -> read
# w -> write
# a -> append
# r+ -> r + w

for x in employee_file.readlines():
    print(x)

# don't forget to close it
employee_file.close()

employee_file = open("./employees.txt", "a")
employee_file.write("\nTOBY")
employee_file.close()