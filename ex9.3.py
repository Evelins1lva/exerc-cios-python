def avoids(word, forbidden):
    for letra in word:
        if letra in forbidden:
            return False
    return True

def analisa_palavras():
    forbidden = input("Digite as letras proibidas (ex: abcde): ").lower()
    count = 0
    total = 0

    try:
        with open("words.txt", "r") as arquivo:
            for linha in arquivo:
                palavra = linha.strip()
                total += 1
                if avoids(palavra, forbidden):
                    count += 1

        print(f"\nTotal de palavras: {total}")
        print(f"Palavras que NÃO contêm nenhuma das letras '{forbidden}': {count}")
        print(f"Porcentagem: {(count/total)*100:.2f}%")

    except FileNotFoundError:
        print("Arquivo 'words.txt' não encontrado. Verifique se está na mesma pasta do script.")

# Executa a função
analisa_palavras()
