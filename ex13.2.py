def processar_livro(nome_arquivo):
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

    total_palavras = len(palavras)

    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1

    print(f"Total de palavras: {total_palavras}")
    print(f"Palavras diferentes: {len(contagem)}")
    
    return contagem
