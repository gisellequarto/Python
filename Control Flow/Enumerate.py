cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for index, cast_name in enumerate(cast):
    cast[index] = cast_name + " " + str(heights[index])

print(cast)