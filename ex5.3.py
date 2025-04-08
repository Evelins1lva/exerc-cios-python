def is_triangle(a, b, c):
    # Verifica a condição do teorema da desigualdade triangular
    if a > b + c or b > a + c or c > a + b:
        print("No")
    else:
        print("Yes")

def test_triangle():
    try:
        a = int(input("Digite o comprimento do primeiro graveto: "))
        b = int(input("Digite o comprimento do segundo graveto: "))
        c = int(input("Digite o comprimento do terceiro graveto: "))
        is_triangle(a, b, c)
    except ValueError:
        print("Por favor, insira apenas números inteiros.")

# Chamada do teste
test_triangle()
