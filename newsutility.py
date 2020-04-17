from newspaper import *
import webbrowser
url="https://www.bbc.com/news/uk-52304914"
cnn_article=Article(url,languages="en")
print(cnn_article.url)
cnn_article.download()
cnn_article.parse()
cnn_article.nlp()
hs=open("1.html",'w')
hs.write(cnn_article.text)
hs.close()
