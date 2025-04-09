import time
import os

def criar_arquivo_exemplo():
    caminho = os.path.join(os.path.dirname(__file__), 'words.txt')
    if not os.path.exists(caminho):
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write('\n'.join(['amor', 'vida', 'esperança', 'força', 'coragem', 'felicidade']))
        print("Arquivo words.txt criado com sucesso!")

def lista_com_append():
    lista = []
    caminho = os.path.join(os.path.dirname(__file__), 'words.txt')
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            palavra = linha.strip()
            lista.append(palavra)
    return lista

def lista_com_concatenacao():
    lista = []
    caminho = os.path.join(os.path.dirname(__file__), 'words.txt')
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            palavra = linha.strip()
            lista = lista + [palavra]
    return lista

if __name__  == "_main_":
    criar_arquivo_exemplo()

    inicio = time.time()
    lista_com_append()
    print("Tempo com append:", time.time() - inicio)

    inicio = time.time()
    lista_com_concatenacao()
    print("Tempo com +:", time.time() - inicio)

