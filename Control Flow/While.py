import math

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here

while current < number:
    product += product * current
    current +=1

    # multiply the product so far by the current number
    
    
    # increment current with each iteration until it reaches number



# print the factorial of number
print(product)



start_num = 5 #provide some start number
end_num = 100 #provide some end number that you stop when you hit
count_by = 2 #provide some number to count by 

break_num = start_num

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num

while break_num < end_num:
    break_num += count_by

print(break_num)



limit = 40
nearest_square = 0

while (nearest_square + 1)**2 < limit:
    nearest_square += 1

nearest_square = nearest_square**2

print(nearest_square)


num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

odd_sum = 0
odd_count = 0

for num in num_list:
    if num % 2 != 0 and odd_count < 5:
        odd_sum += num
        odd_count += 1

print(odd_count)
print(odd_sum)