import nlpwrapper
import time
import logging
import sys


root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

logger = logging.getLogger(__file__)


def __main__():
    ner_server = nlpwrapper.NERServer()
    ner_server.start()


if __name__ == "__main__":
    logger.info("Starting up")
    __main__()
    logger.info("we are asleep")
    time.sleep(30)
    logger.info("wakeup")
