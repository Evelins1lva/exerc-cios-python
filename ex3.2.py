def print_twice(msg):
    print(msg)
    print(msg)

def do_twice(f, valor):
    f(valor)
    f(valor)

def do_four(f, valor):
    do_twice(f, valor)
    do_twice(f, valor)

# Testando
do_twice(print_twice, 'spam')
print('---')
do_four(print_twice, 'Python é legal!')
