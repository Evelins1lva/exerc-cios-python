def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

# Testes
strings_para_testar = [
    "HELLO",
    "Hello",
    "hello",
    "123",
    "HeLLo123abc"
]

for s in strings_para_testar:
    print(f"\nTestando com: '{s}'")
    print("1:", any_lowercase1(s))
    print("2:", any_lowercase2(s))
    print("3:", any_lowercase3(s))
    print("4:", any_lowercase4(s))
    print("5:", any_lowercase5(s))
