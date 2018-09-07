
from generated_api.nlp.spacy import NERExtractor, ttypes
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import spacy
import logging

logger = logging.getLogger(__file__)


class LanguageNotSupportedException(Exception):
    def __init__(self, lang):
        self.lang = lang


class EntityExtractor(object):

    # Mapping so that clients can tell us the trigraph
    MODEL_LANGS = {
        # "DEU": "de",
        "ENG": "en",
        # "FRA": "fr",
        # "ITA": "it",
        # "NET": "nl",  # Netherlands
        # "POR": "pt",
        # "SPA": "es",
    }

    def __init__(self, model_root_path="/home/shaun/work/spacy-models/"):
        self.__model_root_path = model_root_path.rstrip("/")
        self.__nlp_langs = {}

    def load_models(self):
        logger.info("Beginning to load models")
        for tri, bi in EntityExtractor.MODEL_LANGS.items():
            logger.debug("loading model for {} [{}]".format(bi, tri))
            self.__nlp_langs[tri] = spacy.load(self.__model_path_for_lang(bi))
            logger.debug("model for {} [{}] loaded".format(bi, tri))

        logger.info("Loading models complete")

    def models_loaded(self):
        return len(self.__nlp_langs) > 0

    def extract(self, language_trigraph, text):
        if language_trigraph.upper() not in self.__nlp_langs:
            raise LanguageNotSupportedException(language_trigraph.upper())

        return self.__nlp_langs[language_trigraph.upper()](text).ents

    def __model_path_for_lang(self, lang):
        if lang == "en":
            return "{}/{}_core_web_sm/{}_core_web_sm-2.0.0".format(self.__model_root_path, lang, lang)
        return "{}/{}_core_news_sm/{}_core_news_sm-2.0.0".format(self.__model_root_path, lang, lang)


class NERHandler(object):
    def __init__(self, entity_extractor):
        self.__entity_extractor = entity_extractor

    def start(self):
        if not self.__entity_extractor.models_loaded():
            self.__entity_extractor.load_models()

    def entities(self, lang, document_string):
        try:
            spans = list()
            entities = self.__entity_extractor.extract(lang, document_string)
            for e in entities:
                span = ttypes.EntitySpan(text=e.text, entityType=e.label_, startPos=e.start, endPos=e.end)
                spans.append(span)

            return spans
        except LanguageNotSupportedException as lse:
            raise ttypes.UnsupportedLanguage(language=lse.lang)


class NERServer(object):
    def __init__(self, host="127.0.0.1", port=9090, entity_extractor=EntityExtractor()):
        self.__ner_handler = NERHandler(entity_extractor)
        tprocessor = NERExtractor.Processor(self.__ner_handler)
        self.__transport = TSocket.TServerSocket(host=host, port=port)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()

        # TODO: use this TThreadPoolServer
        self.__tserver = TServer.TSimpleServer(tprocessor, self.__transport, tfactory, pfactory)

    def start(self):
        logger.info("starting the ner handler")
        self.__ner_handler.start()
        logger.info("starting the service bind to {}:{}".format(self.__transport.host, self.__transport.port))
        self.__tserver.serve()

