def invert_dict(d):
    resultado = {}
    for chave, valor in d.items():
        resultado.setdefault(valor, []).append(chave)
    return resultado

# Exemplo
original = {'a': 1, 'b': 2, 'c': 1}
invertido = invert_dict(original)
print(invertido)
