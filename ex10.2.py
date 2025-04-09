def cumsum(lista):
    resultado = []
    soma = 0
    for numero in lista:
        soma += numero
        resultado.append(soma)
    return resultado

