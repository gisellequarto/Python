def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename, 'r') as f:
        cast_list = [line.split(',')[0] for line in f]

    return cast_list



cast_list = create_cast_list('Scripts and Errors/flying_circus_cast.txt')
for actor in cast_list:
    print(actor)