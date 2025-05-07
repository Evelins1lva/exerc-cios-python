import traceback
import sys

try:
    # Forçando um erro proposital
    raise Exception("Erro teste - MOSTRAR TRACEBACK COMPLETO")
except Exception as e:
    print("\n=== TRACEBACK COMPLETO ===")
    traceback.print_exc(file=sys.stdout)  # Isso vai mostrar TUDO
    print("=========================\n")
    
    # Alternativa ainda mais detalhada:
    print("\n=== DETALHES DO ERRO ===")
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback, limit=5, file=sys.stdout)