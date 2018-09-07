import ner
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
    # entity_extractor = ner.EntityExtractor()
    # entity_extractor.load_models()
    ner_server = ner.NERServer()
    ner_server.start()
    # sentences = [
    #     "My name is Eminem",
    #     "Apple is looking at buying a U.K. company for $1 billion",
    #     "Foobar is Bazbiz's father"
    # ]
    #
    # for sentence in sentences:
    #     print(sentence)
    #     print("----------------------")
    #     for labeled_word in entity_extractor.extract( "ENG", sentence):
    #         print("{} => [{}] type: ({})\tloc: {} -> {} w/ sentiment: {}"
    #               .format(labeled_word.text,
    #                       labeled_word.label_,
    #                       labeled_word.__class__,
    #                       labeled_word.start,
    #                       labeled_word.end,
    #                       labeled_word.sentiment))


if __name__ == "__main__":
    logger.info("Starting up")
    __main__()
    logger.info("we are asleep")
    time.sleep(30)
    logger.info("wakeup")
