import logging

logging.basicConfig(level=logging.DEBUG)

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        logging.exception("Tentativa de divisão por zero.")
    else:
        logging.info(f"Resultado da divisão: {resultado}")

