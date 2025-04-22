import requests
from bs4 import BeautifulSoup
import logging

# Configurar logging
logging.basicConfig(
    filename='scraping.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def scrape_titulo(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # levanta erro se status != 200
        soup = BeautifulSoup(response.text, 'html.parser')
        titulo = soup.title.string.strip()

        print(f"Título da página: {titulo}")
        logging.info(f"Scraping bem-sucedido da URL: {url}")
        logging.info(f"Título capturado: {titulo}")
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
        logging.error(f"Erro ao fazer scraping de {url} - {e}")

# Teste com exemplo
if __name__ == "__main__":
    url = input("Digite a URL: ")
    scrape_titulo(url)
