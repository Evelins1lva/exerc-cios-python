def uses_all(word, required):
    return all(letra in word for letra in required)

def contar_palavras_com_todas(letras_obrigatorias):
    count = 0

    try:
        with open("words.txt", "r") as arquivo:
            for linha in arquivo:
                palavra = linha.strip().lower()
                if uses_all(palavra, letras_obrigatorias):
                    count += 1

        print(f"Palavras que contêm todas as letras '{letras_obrigatorias}': {count}")

    except FileNotFoundError:
        print("Arquivo 'words.txt' não encontrado. Verifique se está na mesma pasta do script.")

# Testa com vogais 
contar_palavras_com_todas("aeiou")
contar_palavras_com_todas("aeiouy")
