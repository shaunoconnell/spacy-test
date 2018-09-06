
import spacy

MODEL_PATH="/home/shaun/work/spacy-models/en_core_web_lg-2.0.0/en_core_web_lg/en_core_web_lg-2.0.0"

class EntityExtractor(object):
  def __init__(self, model_path):
    self.__nlp = spacy.load(model_path)

  def entities(self, str):
    return self.__nlp(str).ents

def __main__():
  entity_extractor = EntityExtractor(MODEL_PATH)

  sentences = [
    "My name is Eminem",
    "Apple is looking at buying a U.K. company for $1 billion",
    "Foobar is Bazbiz's father"
  ]

  for sentence in sentences:
    print(sentence)
    print("----------------------")
    for labeled_word in entity_extractor.entities(sentence):
      print("{} => [{}] type: ({})\tloc: {} -> {} w/ sentiment: {}"
            .format(labeled_word.text,
                    labeled_word.label_,
                    labeled_word.__class__,
                    labeled_word.start,
                    labeled_word.end,
                    labeled_word.sentiment))


if __name__ == "__main__":
  __main__()
