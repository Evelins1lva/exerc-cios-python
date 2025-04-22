import logging
logger = logging.getLogger('meu_logger')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('meu_logger.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug("Esta é uma mensagem de depuração.")
logger.info("Esta é uma mensagem informativa.")
logger.warning("Esta é uma mensagem de aviso.")
logger.error("Esta é uma mensagem de erro.")
logger.critical("Esta é uma mensagem crítica.")
