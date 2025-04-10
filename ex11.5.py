def rotate_word(word, n):
    return word[n:] + word[:n]

def find_rotate_pairs(words):
    pairs = []
    for word in words:
        for i in range(1, len(word)):
            rotated = rotate_word(word, i)
            if rotated in words and (rotated, word) not in pairs:
                pairs.append((word, rotated)) 
    return pairs  
# Lista de palavras
words = ['abc', 'bca', 'cab', 'cba', 'gca', 'oie', 'bom']

# Encontrar e mostrar os pares
result = find_rotate_pairs(words)
for pair in result:
    print(pair)
