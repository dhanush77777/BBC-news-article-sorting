import requests      
#testing
api_key="706c4dbcb4ac484a9c9c2488add37812"


main_url="https://newsapi.org/v2/top-headlines?country=in&category=politics&apiKey="+api_key
news=requests.get(main_url).json()
article=news["articles"]
    
    
news_article=[]
n=[]
for arti in article:
    news_article.append(arti['title'])
        #print(news_article)
for i in range(5):
    n.append(news_article[i])
    
print(n)   