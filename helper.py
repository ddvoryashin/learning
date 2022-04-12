import logging
logger = logging.getLogger(__name__)
logger.propagate = False # it won't write anything
logger.info('hello from helper')
