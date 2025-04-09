# Dicionário para armazenar os resultados que já foram  calculados
memo = {}

def ack(m, n):
    if (m, n) in memo:
        return memo[(m, n)]
    
    if m == 0:
        resultado = n + 1
    elif n == 0:
        resultado = ack(m - 1, 1)
    else:
        resultado = ack(m - 1, ack(m, n - 1))
    
    memo[(m, n)] = resultado
    return resultado

# Teste
print("Resultado de ack(3, 4):", ack(3, 4))
