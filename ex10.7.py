def has_duplicates(lista):
    for item in lista:
        if lista.count(item) > 1:
            return True
    return False
# Testes
if __name__ == "__main__":
    print(has_duplicates([1, 2, 3, 4]))     
    print(has_duplicates([1, 2, 2, 3]))     
    print(has_duplicates(['a', 'b', 'a'])) 
