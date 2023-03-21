first_name = 'Nick'
# $ These are strings
last_name = 'Naps'
full_name = first_name + last_name
print("Hello nerd " + full_name)

# $ These are ints
age = 21
# % age += 1 or age = age + 1 - they're both the same thing
print(age)
print(type(age))

# print("Your age is " + age) # ! Will not work because a str cannot concatenate with an int so you must TYPECAST
print("Your age is " + str(age))

# $ floats
height = 250.5
print(height)
print(type(height))

# $ Booleans
human = False
print(human)
print('Are you a human?: ' + str(human))
print(type(human))
