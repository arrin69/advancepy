import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger(__name__)
logger.debug("this is debug log")
logger.warning("this is warn log")
logger.info("this is info log")
logger.critical("this is critical log")
logger.error("this is an error !")


