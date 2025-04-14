def children(word, word_set):
    return [word[:i] + word[i+1:] for i in range(len(word)) if word[:i] + word[i+1:] in word_set]

def is_reducible(word, word_set, memo):
    if word in memo:
        return memo[word]
    if word == "":
        return True
    for child in children(word, word_set):
        if is_reducible(child, word_set, memo):
            memo[word] = True
            return True
    memo[word] = False
    return False

def all_reducible_words(word_set):
    memo = {}
    return [word for word in word_set if is_reducible(word, word_set, memo)]

def main():
    word_set = load_words()
    reducible_words = all_reducible_words(word_set)
    if reducible_words:
        longest = max(reducible_words, key=len)
        print("Palavra mais longa redutível:", longest)
        print("Número de letras:", len(longest))
    else:
        print("Nenhuma palavra redutível encontrada.")

main()
