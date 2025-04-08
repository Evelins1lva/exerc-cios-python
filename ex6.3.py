def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):

    if len(word) <= 1:
        return True
    
    if first(word) != last(word):
        return False
    
    return is_palindrome(middle(word))


# Testes
print("reviver é palíndromo?", is_palindrome("reviver"))  
print("osso é palíndromo?", is_palindrome("osso"))        
print("python é palíndromo?", is_palindrome("python"))    
print("a é palíndromo?", is_palindrome("a"))              
print("'' (vazio) é palíndromo?", is_palindrome(""))      
print("ab é palíndromo?", is_palindrome("ab"))            
