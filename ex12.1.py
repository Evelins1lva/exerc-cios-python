def most_frequent(s):
    
    freq = {}
    
  
    for char in s.lower():
        if char.isalpha(): 
            freq[char] = freq.get(char, 0) + 1
    
    # Ordena as letras em ordem decrescente de frequência
    sorted_letters = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    
    # Exibe as letras e suas frequências
    for letter, count in sorted_letters:
        print(f"{letter}: {count}")

# Exemplo de uso
texto = "exemplo de texto para frequência de letras."
most_frequent(texto)
