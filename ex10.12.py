def interligar(p1, p2):
    nova = ''
    for i in range(len(p1)):
        nova += p1[i] + p2[i]
    return nova

def encontrar_interligadas(lista):
    for p1 in lista:
        for p2 in lista:
            if len(p1) == len(p2):
                combinada = interligar(p1, p2)
                if combinada in lista:
                    print(f"{p1} + {p2} → {combinada}")

# Lista de palavras
palavras = ['shoe', 'cold', 'schooled', 'sol', 'mar', 'somar', 'roma', 'amor']

encontrar_interligadas(palavras)
