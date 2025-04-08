def is_palindrome(s):
    return s == s[::-1]

def verificar_odometro():
    for n in range(100000, 1000000): 
        s = str(n)
        if is_palindrome(s[2:]):
            s1 = str(n + 1)
            if is_palindrome(s1[1:]):
                s2 = str(n + 2)
                if is_palindrome(s2[1:5]):
                    s3 = str(n + 3)
                    if is_palindrome(s3):
                        print(f"🔍 Número inicial do hodômetro: {n}")
                        print(f"{n}: últimos 4 → {s[2:]}")
                        print(f"{n+1}: últimos 5 → {s1[1:]}")
                        print(f"{n+2}: 4 centrais → {s2[1:5]}")
                        print(f"{n+3}: todos os 6 → {s3}")
                        print("-" * 30)

verificar_odometro()
