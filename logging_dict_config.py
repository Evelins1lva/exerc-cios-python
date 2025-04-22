import logging
import logging.config

log_config = {
    'version': 1,
    'formatters': {
        'formato_simples': {
            'format': '%(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'formato_simples',
            'level': 'DEBUG',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

logging.config.dictConfig(log_config)

logging.debug("Mensagem de depuração.")
logging.info("Mensagem informativa.")
logging.warning("Mensagem de aviso.")
logging.error("Mensagem de erro.")
logging.critical("Mensagem crítica.")
