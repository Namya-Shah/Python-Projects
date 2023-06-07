from googlesearch import search

query = input("Enter what you want to ask Google: ")

for i in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(i)