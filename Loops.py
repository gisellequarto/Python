sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line
for word in sentence:
    print(word)



# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
for n in range(5, 31, 5):
    print(n)


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"))


print(usernames)

usernames2 = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for index in range(len(usernames2)):
    usernames2[index] = usernames2[index].lower().replace(" ", "_")


print(usernames2)


tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == "<" and token.endswith(">"):
        count +=1

print(count)



items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>" + item + "</li>\n"

html_str += "</ul>"

print(html_str)