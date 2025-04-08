def eval_loop():
    ultimo_resultado = None
    while True:
        entrada = input("Digite uma expressão (ou 'done' para sair): ")
        if entrada == 'done':
            break
        try:
            ultimo_resultado = eval(entrada)
            print(ultimo_resultado)
        except Exception as e:
            print("Erro:", e)
    print("Último resultado avaliado:", ultimo_resultado)

# Chamada da função
eval_loop()
