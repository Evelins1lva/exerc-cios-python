# Exercício 1.2 

# 1. 
minutos = 42
segundos = 42
total_segundos = minutos * 60 + segundos
print("Total de segundos:", total_segundos)

# 2. 
# Dica: 1 milha = 1.61 km
km = 10
milhas = km / 1.61
print("10 km em milhas:", milhas)

# 3. 
# a) 
tempo_total_min = minutos + segundos / 60
passo_medio_min = tempo_total_min / milhas

minutos_passo = int(passo_medio_min)
segundos_passo = (passo_medio_min - minutos_passo) * 60
print(f"Passo médio: {minutos_passo} min e {round(segundos_passo)} s por milha")

# b) 
tempo_horas = tempo_total_min / 60
velocidade_mph = milhas / tempo_horas
print("Velocidade média (mph):", round(velocidade_mph, 2))
