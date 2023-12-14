# https://newsapi.org/account 
# 159470d835f543fb8ff1454c865b269b

import requests

r = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2023-11-14&sortBy=publishedAt&apiKey=159470d835f543fb8ff1454c865b269b')
contenet = r.json()
# print(type(contenet))
articles = contenet['articles']

for article in articles:
    print(article)