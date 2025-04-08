import math

def estimate_pi():
    total = 0
    k = 0
    while True:
        num = math.factorial(4*k) * (1103 + 26390*k)
        den = math.factorial(k)**4 * 396**(4*k)
        termo = (2 * math.sqrt(2) / 9801) * (num / den)
        total += termo
        if termo < 1e-15:
            break
        k += 1
    return 1 / total

# Testando
print("Estimativa de π:", estimate_pi())


