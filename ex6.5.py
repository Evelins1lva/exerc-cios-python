def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Testes
print(gcd(48, 18))   
print(gcd(20, 8))    
print(gcd(100, 25))  
print(gcd(17, 13))   
