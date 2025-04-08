
# Usando strip
texto = "   Olá Evelin   "
print("Com espaços:", repr(texto))
print("Sem espaços:", repr(texto.strip()))

# Usando replace
frase = "Eu gosto de maçã"
nova_frase = frase.replace("maçã", "banana")
print("Frase original:", frase)
print("Frase nova:", nova_frase)

# Usando find
nome = "Evelin"
print("Posição da letra 'v':", nome.find("v"))
print("Posição da letra 'x':", nome.find("x"))  # Não existe, vai dar -1
