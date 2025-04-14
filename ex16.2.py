from datetime import datetime, timedelta

def exibir_dia_semana():
    hoje = datetime.today()
    dia_semana = hoje.strftime("%A")
    print(f"Hoje é {dia_semana}")

def idade_e_tempo_para_aniversario():
    nascimento_str = input("Digite sua data de nascimento (AAAA-MM-DD): ")
    nascimento = datetime.strptime(nascimento_str, "%Y-%m-%d")
    hoje = datetime.today()

    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    ano_atual = hoje.year
    proximo_aniversario = datetime(year=ano_atual, month=nascimento.month, day=nascimento.day)
    if proximo_aniversario < hoje:
        proximo_aniversario = proximo_aniversario.replace(year=ano_atual + 1)

    tempo = proximo_aniversario - hoje
    print(f"Idade: {idade} anos")
    print(f"Faltam {tempo.days} dias, {tempo.seconds // 3600} horas, {(tempo.seconds % 3600) // 60} minutos e {tempo.seconds % 60} segundos para seu próximo aniversário.")

def dia_duplo():
    data1_str = input("Data de nascimento da primeira pessoa (AAAA-MM-DD): ")
    data2_str = input("Data de nascimento da segunda pessoa (AAAA-MM-DD): ")

    data1 = datetime.strptime(data1_str, "%Y-%m-%d")
    data2 = datetime.strptime(data2_str, "%Y-%m-%d")

    mais_velha, mais_nova = sorted([data1, data2])
    diferenca = mais_nova - mais_velha
    dia_duplo = mais_nova + diferenca

    print(f"O Dia Duplo será em: {dia_duplo.strftime('%Y-%m-%d')}")

def n_vezes_mais_velho():
    data1_str = input("Data da primeira pessoa (AAAA-MM-DD): ")
    data2_str = input("Data da segunda pessoa (AAAA-MM-DD): ")
    n = float(input("Digite o valor de N (ex: 1.5, 2, 3): "))

    data1 = datetime.strptime(data1_str, "%Y-%m-%d")
    data2 = datetime.strptime(data2_str, "%Y-%m-%d")

    mais_velha, mais_nova = sorted([data1, data2])
    diferenca = mais_nova - mais_velha
    dia_n_vezes = mais_nova + (diferenca / (n - 1))

    print(f"A pessoa mais velha será {n} vezes mais velha no dia: {dia_n_vezes.strftime('%Y-%m-%d')}")

# Menu simples
def main():
    print("Escolha o exercício:")
    print("1 - Dia da semana de hoje")
    print("2 - Idade e tempo até o próximo aniversário")
    print("3 - Dia Duplo (uma pessoa tem o dobro da idade da outra)")
    print("4 - N vezes mais velho")

    escolha = input("Digite sua escolha (1 a 4): ")

    if escolha == "1":
        exibir_dia_semana()
    elif escolha == "2":
        idade_e_tempo_para_aniversario()
    elif escolha == "3":
        dia_duplo()
    elif escolha == "4":
        n_vezes_mais_velho()
    else:
        print("Opção inválida.")

if __name__ == "_main_":
    main()
