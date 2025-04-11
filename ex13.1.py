import string

def processar_arquivo(nome_arquivo):
    palavras_processadas = []

    with open(nome_arquivo, 'r') as arquivo:  # ← LINHA 5
        for linha in arquivo:
            palavras = linha.strip().split()

            for palavra in palavras:
                palavra = palavra.strip(string.punctuation)
                palavra = palavra.lower()
                if palavra:
                    palavras_processadas.append(palavra)

    return palavras_processadas  # ← LINHA 18
