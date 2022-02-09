import logging
from logging.handlers import SocketHandler, DEFAULT_TCP_LOGGING_PORT

# logging.warning('Watch out!')  # will print a message to the console
# logging.info('I told you so')


def init_logging(config):
    logger = logging.getLogger(__name__)
    socketHandler = SocketHandler('localhost', DEFAULT_TCP_LOGGING_PORT)
    socketHandler.setLevel(config['LOG_LEVEL'])
    socketHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    logger.addHandler(socketHandler)
    logger.setLevel(config['LOG_LEVEL'])

    return logger


if __name__ == "__main__":
    logger = init_logging({"LOG_LEVEL":logging.DEBUG})
    # logger.debug('S'*100)
    logger.debug(logging.makeLogRecord({"msg":"S"*100}))
