from collections import defaultdict

def obter_palavras():
    return [
        "deltas", "dessalinizar", "durou", "salgado", "agendado", "passado",
        "retenções", "ternários", "gerando", "engrandecendo",
        "refunde", "fundidores", "indefinido",
        "roma", "amor", "pato", "topa", "casa", "saca", "luz"
    ]
    
def encontrar_anagramas(palavras):
    dicionario = {}

    for palavra in palavras:
        chave = ''.join(sorted(palavra.lower()))

        if chave in dicionario:
            dicionario[chave].append(palavra)
        else:
            dicionario[chave] = [palavra]

    # anagramas 
    anagramas = []
    for grupo in dicionario.values():
        if len(grupo) > 1:
            anagramas.append(grupo)

    return anagramas


palavras = ["roma", "amor", "pato", "topa", "casa", "saca", "luz"]

# função
resultado = encontrar_anagramas(palavras)

# anagramas encontrados
for grupo in resultado:
    print(grupo)
