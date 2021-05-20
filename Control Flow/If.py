points = 174  # use this input to make your submission

# write your if statement here
if points > 180:
    result = "Congratulations! You won a penguin!"
elif points > 150:
    result = "Congratulations! You won a wafer-thin mint!"
elif points > 50:
    result = "Oh dear, no prize this time."
elif points > 0:
    result = "Congratulations! You won a wooden rabbit!"

print(result)