
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from nlpapi.spacy import NERExtractor


class NERClient(object):
    def __init__(self, host, port):
        # Make socket
        tsocket = TSocket.TSocket(host, port)

        # Buffering is critical. Raw sockets are very slow
        self.__transport = TTransport.TBufferedTransport(tsocket)

        # Wrap in a protocol
        protocol = TBinaryProtocol.TBinaryProtocol(self.__transport)

        # Create a client to use the protocol encoder
        self.__client = NERExtractor.Client(protocol)

    def start(self):
        self.__transport.open()

    def close(self):
        self.__transport.close()

    def entities(self, lang_trigraph, text):
        return self.__client.entities(lang_trigraph, text)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.close()
