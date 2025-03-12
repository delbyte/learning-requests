from PIL import Image
from io import BytesIO

import requests
from bs4 import BeautifulSoup

r = requests.get("https://en.wikipedia.org/wiki/Bean")


soup = BeautifulSoup(r.text, 'html.parser')

for child in soup.descendants:
    if child.name:  #what why is this needed
        print(child.name)

for tag in soup.find_all('li'):
    print(tag.text)   
