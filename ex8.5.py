def rotate_word(word, shift):
    result = ''
    for char in word:
        if char.islower():
            # Rotaciona letra minúscula
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        elif char.isupper():
            # Rotaciona letra maiúscula
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char
        else:
            # Mantém outros caracteres
            result += char
    return result

# Parte interativa:
palavra = input("Digite uma palavra ou frase: ")
numero = int(input("Digite o número de rotação (positivo ou negativo): "))

resultado = rotate_word(palavra, numero)
print(f"Resultado rotacionado: {resultado}")
