from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from generated_api.nlp.spacy import NERExtractor, ttypes


# Make socket
transport = TSocket.TSocket('localhost', 9090)

# Buffering is critical. Raw sockets are very slow
transport = TTransport.TBufferedTransport(transport)

# Wrap in a protocol
protocol = TBinaryProtocol.TBinaryProtocol(transport)

# Create a client to use the protocol encoder
client = NERExtractor.Client(protocol)

# Connect!
transport.open()

extracted_entities = client.entities("ENG", "Hello there from over here.  Do you listen to the Beatles? the Beatles net worth exceeds 1 billion dollars")


for ee in extracted_entities:
    print(ee)

transport.close()
