# Função que imprime a linha com os cantos '+' e os traços '-'
# Repetir 4 vezes para formar as colunas
def print_beam4():
    print('+ - - - - ' * 4 + '+')

def print_post4():
    print('|         ' * 4 + '|')

def print_row4():
    print_beam4()
    for _ in range(4):
        print_post4()

def print_grid4():
    for _ in range(4):
        print_row4()
    print_beam4()

# Executa a grade 4x4
print_grid4()
