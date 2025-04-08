import math
def mysqrt(a):
    x = a
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < 0.000001:
            return y
        x = y

def test_square_root():
    print("a  mysqrt(a)     math.sqrt(a)  diff")
    print("-- ------------ ------------ ------------")
    for a in range(1, 10):
        my = mysqrt(a)
        real = math.sqrt(a)
        diff = abs(my - real)
        print(f"{a:<2} {my:<12.6f} {real:<12.6f} {diff:<12.6f}")

# Executando
test_square_root()
