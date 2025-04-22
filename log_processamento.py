import logging

logging.basicConfig(level=logging.DEBUG)

def processar_dados(dados):
    logging.info("Iniciando o processamento dos dados.")
    
    if not dados:
        logging.warning("Lista de dados está vazia.")
        return
    
    for i, item in enumerate(dados):
        logging.debug(f"Processando item {i}: {item}")
        if item < 0:
            logging.error(f"Dado inválido: {item}")
    
    logging.info("Processamento concluído.")

