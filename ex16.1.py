class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

def time_to_int(time):
    """Converte um objeto Time em segundos."""
    return time.hour * 3600 + time.minute * 60 + time.second

def int_to_time(seconds):
    """Converte segundos para um objeto Time."""
    time = Time()
    minutes, time.second = divmod(int(seconds), 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def mul_time(time, n):
    """Multiplica um tempo por um número."""
    total_secs = time_to_int(time) * n
    return int_to_time(total_secs)

def average_pace(total_time, distance):
    """Calcula o passo médio (tempo por unidade de distância)."""
    return mul_time(total_time, 1 / distance)

if __name__ == "__main__":
    tempo_total = Time(1, 30, 0)  
    distancia = 10  # 10 milhas (ou km)

    passo_medio = average_pace(tempo_total, distancia)

    print("Tempo total:", tempo_total)
    print(f"Distância: {distancia} milhas")
    print("Passo médio:", passo_medio)
