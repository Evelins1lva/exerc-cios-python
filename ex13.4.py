def carregar_palavras_validas(nome_arquivo):
    with open(nome_arquivo, encoding='utf-8') as f:
        palavras_validas = set(palavra.strip().lower() for palavra in f)
    return palavras_validas

def processar_livro(nome_arquivo, palavras_validas):
    with open(nome_arquivo, encoding='utf-8') as f:
        linhas = f.readlines()

    inicio = 0
    for i, linha in enumerate(linhas):
        if linha.startswith("*** START OF THIS PROJECT GUTENBERG EBOOK"):
            inicio = i + 1
            break

    texto = ' '.join(linhas[inicio:])

    import string
    texto = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    palavras = texto.split()

    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1

    palavras_incorretas = set(contagem.keys()) - palavras_validas

    print(f"\nTotal de palavras: {len(palavras)}")
    print(f"Palavras diferentes: {len(contagem)}")
    print(f"Palavras desconhecidas: {len(palavras_incorretas)}\n")

    print("Exemplos de palavras desconhecidas:")
    for palavra in list(palavras_incorretas)[:20]:
        print(palavra)

    return palavras_incorretas
