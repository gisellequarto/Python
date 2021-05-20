names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# write your list comprehension here
first_names = [name[:name.find(" ")].lower() for name in names]

print(first_names)

multiples_3 = [x * 3 for x in range(1, 21)]

print(list(multiples_3))



scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, value in scores.items() if value >= 65]
print(passed)