def encontrar_pares_inversos(lista):
    pares = []
    conjunto = set(lista)
    for palavra in lista:
        reversa = palavra[::-1]
        if reversa != palavra and reversa in conjunto:
            pares.append((palavra, reversa))
    return pares

# Exemplo
palavras = ['roma', 'amor', 'mar', 'ram', 'sol', 'los', 'vida']
palavras.sort() 
pares = encontrar_pares_inversos(palavras)
vistos = set()
for p1, p2 in pares:
    if (p2, p1) not in vistos:
        print(f"{p1} <-> {p2}")
        vistos.add((p1, p2))
