import time

# Tempo atual em segundos desde a época
tempo_atual = time.time()

# Número total de dias desde a época
dias_desde_epoca = int(tempo_atual // (24 * 3600))

# Segundos restantes do dia atual
segundos_do_dia = int(tempo_atual % (24 * 3600))

# Hora, minuto e segundo
horas = segundos_do_dia // 3600
minutos = (segundos_do_dia % 3600) // 60
segundos = segundos_do_dia % 60

# Saída
print(f"Dias desde a época: {dias_desde_epoca}")
print(f"Hora atual (GMT): {horas:02d}:{minutos:02d}:{segundos:02d}")
