# Exercise 1
print("Hello World!")
print("Hello are you there?")
print("I'm sad, the world didn't respond to me.")
print("Oh well, I like typing this.")
print("This is fun.")
print('Yay for printing.')
print("I'd much rather you 'not'.")
print("Oh my gosh, the world responded!")
print('Yes, I "did"! This was a test.')
print("Oh, yikes.")

# Exercise 2
# A comment, this is so you can read your program later.
# Anything after the # is ignored by Python.

print("I could have code like this.") # and the comment after is ignored

# You can also use a comment to "disable" or comment out code:
# print("This won't run.")

print("This will run.")
# print("This still won't run.")

# Exercise 3
print("I will now count my chickens:")
print("Hens", 25.0 + 30.0 / 6)
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)
print("Now I will count the eggs:")
print(3.0 + 2.0 + 1 - 5.0 + 4.0 % 2 - 1.0 / 4 + 6.0)
print("Is it true that 3 + 2 < 5 - 7?")
print(3.0 + 2.0 < 5.0 - 7.0)
print("What is 3 + 2?", 3.0 + 2.0)
print("What is 5 - 7?", 5.0 - 7.0)
print("Oh, that's why it's False.")
print("How about some more.")
print("Is it greater?", 5.0 > -2.0)
print("Is it greater or equal?", 5.0 >= -2.0)
print("Is it less or equal?", 5.0 <= -2.0)

# Exercise 4
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_not_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Exercise 5
name = 'Kevin T. Tran'
age = 20 # not a lie
height = 70 # inches
weight = 140 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
height_centimeters = height * 2.54
weight_kgs = weight * 0.453592


# Practice Problem 1
# Write a program to introduce your name, year, major, how many credits and
# classes you are taking, your age, your weight, where you live, and your
# school. All of these have to be in different variables. Then write a story out
# of it. You must put a statement where you are above 21 years old without
# putting that as a string.
name = 'Kevin'
year = "Junior"
major = 'Applied Computational Math Sciences'
credits = 0
classes = 0
age = 20
weight = 140
location = 'Seattle'
school = 'University of Washington'
print(f'Hi, my name is {name}. I am a {year} studying {major} at the {school}.')
print(f'It is', age >= 21, ',that I am greater than 21 years old.')
print(f'I live in {location}.')
print(f'I am taking {classes} classes, which sum up to {credits} credits.')
print('It is nice to meet you.')



# Practice Problem 2
# Write about yourself reading through the Python information section.
print('I was reading through the information section, and I saw the subsection')
print('name "Python', 2,' vs. Python', 3,'". This is something that I have been')
print('continually investigating and now after researching it and reading it.')
print('I understand that Python 3 is not backwards compatible.')
print('Not only that but Python', 2, 'is now no longer being supported in')
print("January of", 2020,'.')
