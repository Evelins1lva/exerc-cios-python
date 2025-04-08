def is_power(a, b):
    # se a for igual a b
    if a == b:
        return True
    # Se a não for divisível por b, não pode ser potência
    if a % b != 0:
        return False
    
    return is_power(a // b, b)

# Testes
print(is_power(8, 2))    
print(is_power(27, 3))    
print(is_power(12, 2))    
print(is_power(1, 1))     
print(is_power(1, 5))     
