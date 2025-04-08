def is_abecedarian(word):
    return list(word) == sorted(word)

def contar_palavras_abecedarian():
    count = 0

    try:
        with open("words.txt", "r") as arquivo:
            for linha in arquivo:
                palavra = linha.strip().lower()
                if is_abecedarian(palavra):
                    count += 1

        print(f"Total de palavras em ordem alfabética: {count}")

    except FileNotFoundError:
        print("Arquivo 'words.txt' não encontrado. Verifique se está na mesma pasta do script.")

# Rodar função
contar_palavras_abecedarian()
