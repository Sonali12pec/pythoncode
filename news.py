import requests
from requests import session
import requests
from bs4 import BeautifulSoup
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)


url = 'https://www.bbc.com/news/uk-52304914'
response=requests.get(url)
hs=open("2.html",'w')
hs.write(response.text)
hs.close()