from newspaper import *
url="https://www.bbc.com/news/uk-52304914"
cnn_article=Article(url,language="en")
print(cnn_article.url)
cnn_article.download()
cnn_article.parse()
cnn_article.nlp()
print(cnn_article.text)
hs=open("2.html",'w')
hs.write(cnn_article.text)
hs.close()