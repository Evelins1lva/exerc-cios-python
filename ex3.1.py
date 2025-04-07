# Exercício 

def right_justify(s):
    # Calcular quantos espaços precisam vir antes da string
    espaços = 70 - len(s)
    
    print(' ' * espaços + s)

right_justify('monty')

# Testes extras
right_justify('Python')
right_justify('Evelin')
right_justify('isso é divertido')
