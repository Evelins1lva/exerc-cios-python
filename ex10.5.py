def is_sorted(lista):
    return lista == sorted(lista)

if __name__ == "__main__":
    print(is_sorted([1, 2, 2]))      
    print(is_sorted(['b', 'a']))     
    print(is_sorted([5, 10, 15]))    
    print(is_sorted([3, 2, 1]))      
