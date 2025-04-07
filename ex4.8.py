# print("Olá!")
# print("Seja bem-vindo ao sistema.")

# Encapsulamento
def saudacao():
    print("Olá!")
    print("Seja bem-vindo ao sistema.")

# Generalização
def saudacao(nome):
    print(f"Olá, {nome}!")
    print("Seja bem-vindo ao sistema.")

# Novas funcionalidades encapsuladas
def exibir_menu():
    print("1. Iniciar")
    print("2. Sair")

# Refatoração do menu com generalização
def exibir_menu(opcoes):
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")

# Função principal que orquestra o programa
def main():
    nome_usuario = input("Digite seu nome: ")
    saudacao(nome_usuario)
    opcoes = ["Iniciar", "Ajuda", "Sair"]
    exibir_menu(opcoes)

# Execução do programa
main()
