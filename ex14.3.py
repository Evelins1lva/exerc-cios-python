import os
import hashlib

def encontrar_arquivos(diretorio_raiz, sufixo='.mp3'):
    
    arquivos = []
    for pasta_atual, subpastas, arquivos_na_pasta in os.walk(diretorio_raiz):
        for nome_arquivo in arquivos_na_pasta:
            if nome_arquivo.lower().endswith(sufixo):
                caminho_completo = os.path.join(pasta_atual, nome_arquivo)
                arquivos.append(caminho_completo)
    return arquivos

def calcular_md5(caminho_arquivo):
    
    hash_md5 = hashlib.md5()
    try:
        with open(caminho_arquivo, "rb") as f:
            for bloco in iter(lambda: f.read(4096), b""):
                hash_md5.update(bloco)
    except Exception as e:
        print(f"Erro ao ler {caminho_arquivo}: {e}")
        return None
    return hash_md5.hexdigest()

def encontrar_duplicatas(diretorio, sufixo='.mp3'):
    arquivos = encontrar_arquivos(diretorio, sufixo)
    print(f"{len(arquivos)} arquivos encontrados com sufixo {sufixo}")

    hash_map = {}
    for arquivo in arquivos:
        hash_md5 = calcular_md5(arquivo)
        if hash_md5:
            hash_map.setdefault(hash_md5, []).append(arquivo)

    duplicatas = [grupo for grupo in hash_map.values() if len(grupo) > 1]
    return duplicatas
