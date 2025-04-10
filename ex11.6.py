homofonos = ["cela", "sinto", "imigrar ", "cassar", "concerto", "maçã", "também"]
# Lista base pra testar
word_list = ["cela", "sinto", "imigrar", "cassar", "concerto", "maçã", "também"]

for word in word_list:
    if len(word) == 5:
        word1 = word[1:]              # sem a primeira letra
        word2 = word[0] + word[2:]    # sem a segunda letra

        # Verificar se todas as palavras estão na lista de homófonos
        if word in homofonos and word1 in homofonos and word2 in homofonos:
            print(word, word1, word2)
