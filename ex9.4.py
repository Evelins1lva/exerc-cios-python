def uses_only(word, allowed):
    return all(letra in allowed for letra in word)

# Letras permitidas
permitidas = "acefhlo"

# Frase que só usa essas letras
frase = "a chef of local hole"

# Mostra resultado para cada palavra da frase
for palavra in frase.split():
    if uses_only(palavra, permitidas):
        print(f"'{palavra}' ✅ usa só letras permitidas")
    else:
        print(f"'{palavra}' ❌ usa letras proibidas")

