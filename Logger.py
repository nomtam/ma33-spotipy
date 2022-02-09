import logging

import configuration


class Logger:
    logging.basicConfig(filename=configuration.logs_path, level= logging.DEBUG)
    logger = logging.getLogger()
