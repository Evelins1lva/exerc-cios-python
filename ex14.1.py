def sed(padrao, substituicao, arquivo_origem, arquivo_destino):
    try:
        with open(arquivo_origem, 'r') as f_origem:
            linhas = f_origem.readlines()

        with open(arquivo_destino, 'w') as f_destino:
            for linha in linhas:
                nova_linha = linha.replace(padrao, substituicao)
                f_destino.write(nova_linha)

    except FileNotFoundError:
        print(f"Erro: o arquivo '{arquivo_origem}' não foi encontrado.")
    except IOError as e:
        print(f"Erro de entrada/saída: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
