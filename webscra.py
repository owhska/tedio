# import requests 
# from bs4 import BeautifulSoup
# 
# url = "https://quotes.toscrape.com"
# 
# response = requests.get(url) # faz uma requisicao na url 
# 
# html = response.text # pega o html
# 
# soup = BeautifulSoup(html, "html.parser") # analise o html da pagina
# 
# quotes = soup.find_all("span", class_="text") # faz a procura de elementos
# 
# for quote in quotes:
    # print(quote.text)

import requests 
from bs4 import BeautifulSoup

url = "https://docs.python.org/3/"

response = requests.get(url) # faz uma requisicao na url 

html = response.text # pega o html

soup = BeautifulSoup(html, "html.parser") # analise o html da pagina

divs = soup.find_all("a") # faz a procura de elementos

for div in divs:
    print(div.text)
