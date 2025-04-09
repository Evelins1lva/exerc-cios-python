def has_duplicates(lista):
    vistos = {}
    for item in lista:
        if item in vistos:
            return True
        vistos[item] = True
    return False
# Testes
if __name__ == "__main__":
    print(has_duplicates([1, 2, 3, 4]))     
    print(has_duplicates([1, 2, 2, 3]))     
    print(has_duplicates(['a', 'b', 'a'])) 
