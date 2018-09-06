
import spacy
import random

MODEL_PATH="/home/shaun/work/spacy-models/en_core_web_lg-2.0.0/en_core_web_lg/en_core_web_lg-2.0.0"


TRAIN_DATA = [
    ('Who is Shaka Khan?', {
        'entities': [(7, 17, 'PERSON')]
    }),
    ('I like London and Berlin.', {
        'entities': [(7, 13, 'LOC'), (18, 24, 'LOC')]
    }),
    ('Do you listen to Fugazi or the Beatles', {
        'entities': [(17, 23, 'ORG'), (31,38, 'ORG')]
    })
]

TRAINING_ITERATIONS = 10

nlp = spacy.load(MODEL_PATH)
ner = nlp.get_pipe('ner')


def print_training_data():
    for train_item in TRAIN_DATA:
        print("----------------------------------")
        print(train_item[0])
        found_entities = nlp(train_item[0]).ents
        for fe in found_entities:
            print("{}:[{}]".format(fe.label_, fe.text))

print_training_data()

# get names of other pipes to disable them during training
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):  # only train NER
    optimizer = nlp.begin_training()
    for itn in range(TRAINING_ITERATIONS):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            nlp.update(
                [text],  # batch of texts
                [annotations],  # batch of annotations
                drop=0.5,  # dropout - make it harder to memorise data
                sgd=optimizer,  # callable to update weights
                losses=losses)
        print(losses)

print_training_data()



