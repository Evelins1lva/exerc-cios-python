def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

def test_fermat():
    try:
        a = int(input("Digite um valor inteiro para a: "))
        b = int(input("Digite um valor inteiro para b: "))
        c = int(input("Digite um valor inteiro para c: "))
        n = int(input("Digite um valor inteiro para n (maior que 2): "))
        check_fermat(a, b, c, n)
    except ValueError:
        print("Por favor, insira apenas números inteiros")
              
test_fermat()
