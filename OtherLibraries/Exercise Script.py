# Write your code here
# HINT: create a dictionary from flowers.txt
def create_flowers_dict(filename):
    flw_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            flw_list = line.replace('\n', '').split(': ')
            flw_dict[flw_list[0]] = flw_list[1]
    
    return flw_dict

# HINT: create a function to ask for user's first and last name
def main():
    flower_dict = create_flowers_dict('OtherLibraries/flowers.txt')

    #Getting the first letter
    first_letter =  input("Enter your First [space] Last name only: ").title().split(" ")[0][0]

    # print the desired output
    print('Unique flower name with the {} letter: {}'.format(first_letter, flower_dict[first_letter]))

main()