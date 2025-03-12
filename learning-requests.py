from PIL import Image
from io import BytesIO

import requests
import bs4

r = requests.get("https://en.wikipedia.org/wiki/Bean")
i = Image.open(BytesIO(r.content))


print(r.content)

