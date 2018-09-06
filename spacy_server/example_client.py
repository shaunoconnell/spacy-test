from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from generated_api.nlp.spacy import NLP, ttypes


# Make socket
transport = TSocket.TSocket('localhost', 9090)

# Buffering is critical. Raw sockets are very slow
transport = TTransport.TBufferedTransport(transport)

# Wrap in a protocol
protocol = TBinaryProtocol.TBinaryProtocol(transport)

# Create a client to use the protocol encoder
client = NLP.Client(protocol)

# Connect!
transport.open()

extracted_entities = client.entities("Hello there from over here")

for ee in extracted_entities:
    print(ee)

transport.close()
