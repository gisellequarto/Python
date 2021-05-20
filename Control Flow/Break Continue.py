# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here

for line in headlines:
    print(len(line))
    if len(news_ticker + line) > 140:
        for letter in line:
            if (len(news_ticker + letter)) > 140:
                break
            news_ticker += letter
        break
    news_ticker += line + " "

print(len(news_ticker))
print(news_ticker)