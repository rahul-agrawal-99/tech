import requests
import re
from bs4 import BeautifulSoup

topic =  "doge"

res = requests.get("https://www.google.com/search?q=news+on+{}&sxsrf=APq-WBssrD7ZdlNNQHpEVJrzidpok1p5GA:1649831618791&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjm1s7ctZD3AhW-ldgFHWLbDtUQ_AUoAXoECAEQAw&cshid=1649831634394851&biw=1707&bih=802&dpr=1.13".format(topic))   
# res = requests.get("https://www.google.com/search?q=news+on+{}".format(topic))   


source = res.content

soup = BeautifulSoup(source, 'html.parser')

text =  soup.find_all('div')

pattern = r"\d+"

for txt in text:
    # txt = str(txt)
    print(txt.text)
    # x = re.findall(pattern, txt)
    # print(x)

