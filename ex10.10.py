def in_bisect(lista, alvo):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            baixo = meio + 1
        else:
            alto = meio - 1
    return None
# Exemplo
palavras = ['amor', 'beleza', 'coragem', 'esperança', 'fé', 'paz', 'vida']
palavras.sort()  # Garante a lista ordenada

print(in_bisect(palavras, 'paz'))      
print(in_bisect(palavras, 'alegria'))  
