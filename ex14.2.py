# anagram_sets.py

def read_words(filename):
    """Lê as palavras de um arquivo e retorna uma lista."""
    with open(filename, 'r') as f:
        return [line.strip().lower() for line in f]

def build_anagram_dict(words):
    """Cria um dicionário que mapeia palavras ordenadas para seus anagramas."""
    d = {}
    for word in words:
        key = ''.join(sorted(word))
        d.setdefault(key, []).append(word)
    return d

# Exemplo: usando um arquivo de palavras chamado 'words.txt'
all_anagrams = build_anagram_dict(read_words('words.txt'))
