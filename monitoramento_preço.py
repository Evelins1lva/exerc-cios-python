import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import logging
import re  # Importando a biblioteca re para usar expressões regulares

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "pt-BR"
}

PRODUTO_BUSCA = "martelo"
URL = "https://www.sodimac.com.br/sodimac-br/search?Ntt=martelo"
INTERVALO = 3600  # 1 hora

def buscar_precos():
    logger.info(f"Requisitando a {URL=} com {HEADERS=} e timeout=15")
    response = requests.get(URL, headers=HEADERS, timeout=15)
    logger.info(f"Resultado do {response=}")
    response.raise_for_status()

    try:
        soup = BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        logger.error(f"Falha ao definir soup: {e}")
    else:
        logger.info(f"Sucesso ao definir soup")

    produtos = soup.select('div.product')
    logger.info(f"Quantidade de produtos capturados: {len(produtos)}")

    dados = []
    for i, produto in enumerate(produtos[:5]):  # Limita a 5 resultados
        logger.debug(f"Processando o item {i}")
        try:
            nome_elem = produto.select_one('h2.product-title')
            nome = nome_elem.get_text(strip=True) if nome_elem else "N/A"

            # Selecionando o preço com o seletor correto
            preco_elem = produto.select_one('div.price')  # Ajuste o seletor conforme necessário
            if preco_elem:
                preco_texto = preco_elem.get_text(strip=True)
                # Usando regex para capturar apenas o número após "R$"
                match = re.search(r'R\$ ?([\d.,]+)', preco_texto)
                preco = match.group(1) if match else "N/A"
            else:
                preco = "N/A"

            dados.append({
                "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "produto": nome,
                "preco": preco
            })
        except Exception as prod_error:
            print(f"\n⚠️ Erro ao processar produto: {prod_error}")
            continue

    return dados

def salvar_csv(dados):
    try:
        with open('precos_sodimac.csv', 'a', newline='', encoding='utf-8') as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=["data", "produto", "preco"])
            if arquivo.tell() == 0:
                writer.writeheader()
            writer.writerows(dados)
        print("\n✅ Dados salvos em precos_sodimac.csv")
    except Exception as e:
        print(f"\n⚠️ ERRO AO SALVAR CSV: {e}")

if __name__ == "_main_":
    print(f"\nIniciando busca em {datetime.now().strftime('%d/%m/%Y %H:%M')}...")
    dados = buscar_precos()
    salvar_csv(dados)

