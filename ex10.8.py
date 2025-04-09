# Aniversário Paradoxo
import random
def has_duplicates(lista):
    for item in lista:
        if lista.count(item) > 1:
            return True
    return False

def aniversario_simulacao(n_simulacoes, n_pessoas):
    repeticoes = 0
    for _ in range(n_simulacoes):
        aniversarios = [random.randint(1, 365) for _ in range(n_pessoas)]
        if has_duplicates(aniversarios):
            repeticoes += 1
    probabilidade = repeticoes / n_simulacoes
    return probabilidade
# Executando a simulação
if __name__ == "__main__":
    prob = aniversario_simulacao(10000, 23)
    print(f"Probabilidade estimada de pelo menos duas pessoas fazerem aniversário no mesmo dia (23 pessoas): {prob:.2f}")
