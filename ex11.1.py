def criar_dicionario(lista):
    d = {}
    for palavra in lista:
        d[palavra] = True
    return d

dicionario_palavras = criar_dicionario("palavras")

print('paz' in dicionario_palavras)     
print('alegria' in dicionario_palavras) 
