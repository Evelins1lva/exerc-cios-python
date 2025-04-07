# Exercício 

import math

# 1. Volume da esfera
raio = 5
volume = (4/3) * math.pi * raio**3
print("1. Volume da esfera com raio 5:", round(volume, 2))

# 2. Custo total de 60 livros com desconto e frete
preco_capa = 24.95
desconto = 0.4
preco_descontado = preco_capa * (1 - desconto)

frete = 3 + (59 * 0.75)
custo_total = (preco_descontado * 60) + frete
print("2. Custo total de atacado para 60 cópias:", round(custo_total, 2))

# 3. Horário de chegada após corrida
um_km_lento = 8 * 60 + 15
tres_km_rapido = 3 * (7 * 60 + 12)
ultimo_km = um_km_lento

tempo_total = um_km_lento + tres_km_rapido + ultimo_km

saida = 6 * 3600 + 52 * 60
chegada = saida + tempo_total

hora = chegada // 3600
minuto = (chegada % 3600) // 60
segundo = chegada % 60

print(f"3. Horário de chegada: {hora}:{minuto:02d}:{segundo:02d}")
