import sys
import json
import logging
import requests
import random

# Configuração do logging
logging.basicConfig(
    filename='logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

ARQUIVO = 'users.json'

# Carrega os dados do arquivo JSON
def carregar_usuarios():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Salva os dados no arquivo JSON
def salvar_usuarios(usuarios):
    with open(ARQUIVO, 'w') as f:
        json.dump(usuarios, f, indent=4)

# Adiciona um novo usuário
def adicionar_usuario(nome, idade):
    usuarios = carregar_usuarios()
    if nome in usuarios:
        print("Usuário já existe.")
        logging.warning(f"Tentativa de adicionar usuário já existente: {nome}")
    else:
        usuarios[nome] = idade
        salvar_usuarios(usuarios)
        print("Usuário adicionado com sucesso!")
        logging.info(f"Usuário adicionado: {nome}, idade: {idade}")

# Remove um usuário
def remover_usuario(nome):
    usuarios = carregar_usuarios()
    if nome in usuarios:
        del usuarios[nome]
        salvar_usuarios(usuarios)
        print("Usuário removido com sucesso!")
        logging.info(f"Usuário removido: {nome}")
    else:
        print("Usuário não encontrado.")
        logging.warning(f"Tentativa de remover usuário inexistente: {nome}")

# Busca um usuário
def buscar_usuario(nome):
    usuarios = carregar_usuarios()
    if nome in usuarios:
        print(f"# nome: {nome}\n# idade: {usuarios[nome]}")
        logging.info(f"Busca realizada para o usuário: {nome}")
    else:
        print("Usuário não encontrado.")
        logging.warning(f"Busca por usuário inexistente: {nome}")

# Gera e adiciona nomes aleatórios com scraping da 4devs
def gerar_usuarios(qtd):
    url = "https://www.4devs.com.br/ferramentas_online.php"
    payload = {
        'acao': 'gerar_nom_pessoa',
        'sexo': 'I',
        'pontuacao': 'N',
        'txt_qtde': qtd
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        nomes = response.json()

        for nome in nomes:
            idade = random.randint(18, 60)
            adicionar_usuario(nome, idade)

        logging.info(f"{qtd} usuários gerados automaticamente via scraping.")
    except Exception as e:
        print(f"Erro ao obter nomes: {e}")
        logging.error(f"Erro ao fazer scraping: {e}")

# Execução principal
if __name__ == "__main__":
    args = sys.argv

    if len(args) < 3:
        print("Uso:")
        print("  python app.py add \"Nome\" Idade")
        print("  python app.py rm \"Nome\"")
        print("  python app.py search \"Nome\"")
        print("  python app.py scrape Quantidade")
        sys.exit()

    comando = args[1]

    if comando == "add":
        nome = args[2]
        idade = args[3]
        adicionar_usuario(nome, idade)

    elif comando == "rm":
        nome = args[2]
        remover_usuario(nome)

    elif comando == "search":
        nome = args[2]
        buscar_usuario(nome)

    elif comando == "scrape":
        qtd = int(args[2])
        gerar_usuarios(qtd)

    else:
        print("Comando inválido.")
