def nested_sum(lista_aninhada):
    soma = 0
    for sublista in lista_aninhada:
        soma += sum(sublista)
    return soma
# Exemplo de uso
if __name__ == "__main__":
    t = [[1, 2], [3], [4, 5, 6]]
    resultado = nested_sum(t)
    print("Soma dos elementos aninhados:", resultado)
