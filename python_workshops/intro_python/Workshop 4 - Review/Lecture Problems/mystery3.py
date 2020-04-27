# Problem 3: Print out all numbers greater than 10. What about greater than 10 and divisible by 5?
List1 = [1, 5, 25, 23, 30, 49, 70]

# How do we iterate through a list
for val in range(len(List1)):
    print(List1[val])
print()

# How do we check if a value is greater than 10
val = 15
if val > 10:
    print(val)

# Combine the two together
for val in range(len(List1)):
    if List1[val] > 10:
        print(List1[val])
print()

# Greater than 10 and divisible by 5?
for val in range(len(List1)):
    value = List1[val]
    if value > 10 and value % 5 == 0:
        print(List1[val])
