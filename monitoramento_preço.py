import requests
from bs4 import BeautifulSoup

url = "https://www.sodimac.com.br/sodimac-br/category/cat170014/vaso-sanitario/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Cada produto está dentro de uma tag <div> com uma classe específica
produtos = soup.find_all("div", class_="jsx-3854682921 container jsx-1802958415")

for produto in produtos:
    nome = produto.find("span", class_="jsx-3854682921 product-name")
    preco = produto.find("span", class_="jsx-3854682921 normal-price")

    if nome and preco:
        print(f"{nome.text.strip()} - {preco.text.strip()}")