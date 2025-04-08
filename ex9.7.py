def has_three_double_pairs(word):
    i = 0
    count = 0

    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count += 1
            i += 2  
            if count == 3:
                return True
        else:
            count = 0
            i += 1
    return False


def procurar_palavras_com_tres_pares():
    try:
        with open("words.txt", "r") as arquivo:
            for linha in arquivo:
                palavra = linha.strip()
                if has_three_double_pairs(palavra.lower()):
                    print(f"🔍 Palavra encontrada: {palavra}")

    except FileNotFoundError:
        print("Arquivo 'words.txt' não encontrado. Coloque-o na mesma pasta do script.")


procurar_palavras_com_tres_pares()
