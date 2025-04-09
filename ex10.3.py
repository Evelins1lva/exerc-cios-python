# middle.py

def middle(lista):
    return lista[1:-1]

if __name__ == "__main__":
    t = [1, 2, 3, 4]
    print("Lista original:", t)
    print("Lista do meio:", middle(t))
