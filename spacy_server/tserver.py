from generated_api.nlp.spacy import NLP, ttypes
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import logging

logger = logging.getLogger(__file__)

class NLPWrapper(object):
    def __init__(self):
        pass

    def entities(self, document_string):
        logger.info("ok we are in the document_string")
        spans = list()

        span = ttypes.EntitySpan()
        span.text = "ok"
        span.entityType = "WORD"
        span.startPos = 0
        span.endPos = 1

        spans.append(span)
        return spans


handler = NLPWrapper()
processor = NLP.Processor(handler)
transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

server.serve()

