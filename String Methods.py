# Write two lines of code below, each assigning a value to a variable

greeting = "Hello"
person = "world"

# Now write a print statement using .format() to print out a sentence and the 
#   values of both of the variables
print("We always say: {}, {}!".format(greeting, person))

new_str = "The cow jumped over the moon."
print(new_str.split())
print(new_str.split(' ', 3))
print(new_str.split('.'))

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
print(len(verse))
print(verse.find("and"))
print(verse.rfind("you"))
print(verse.count("you"))