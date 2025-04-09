def chop(lista):
    if len(lista) > 1:
        del lista[0]
        del lista[-1]

if __name__ == "__main__":
    t = [1, 2, 3, 4]
    print("Antes:", t)
    print("Retorno da função:", chop(t))
    print("Depois:", t)
