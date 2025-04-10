# verificação métafase 
def são_metátese(p1, p2):
    dif = [(a, b) for a, b in zip(p1, p2) if a != b]
    return len(dif) == 2 and dif[0] == dif[1][::-1]

# Lista de palavras para teste
palavras = ["conserve", "converse", "listen", "silent", "enlist", "cat", "tac", "act"]

# Encontrar pares de metátese
pares_metatese = [(p1, p2) for p1 in palavras for p2 in palavras if p1 != p2 and são_metátese(p1, p2)]

# Exibir resultados
for p1, p2 in pares_metatese:
    print(f"{p1} <--> {p2}")
