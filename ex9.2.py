def has_no_e(word):
    return 'e' not in word

def analisa_arquivo():
    try:
        total = 0
        sem_e = 0

        with open("words.txt", "r") as arquivo:
            for linha in arquivo:
                palavra = linha.strip()
                total += 1
                if has_no_e(palavra):
                    print(palavra)
                    sem_e += 1

        # Calcula e exibe a porcentagem
        if total > 0:
            porcentagem = (sem_e / total) * 100
            print(f"\nPalavras sem 'e': {sem_e}/{total} ({porcentagem:.2f}%)")
        else:
            print("O arquivo está vazio.")

    except FileNotFoundError:
        print("O arquivo 'words.txt' não foi encontrado. Certifique-se de que ele está na mesma pasta do script.")

# Executa a função principal
analisa_arquivo()
