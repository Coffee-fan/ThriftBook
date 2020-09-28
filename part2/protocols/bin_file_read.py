# Apache Thrift Binary Protocol Struct 2.0 Writer in Python

from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

from thrift import Thrift

class Trade:
    def __init__(self):
        symbol=""
        price=0.0
        size=0

trans = TTransport.TFileObjectTransport(open("data.comp","rb"))
proto = TCompactProtocol.TCompactProtocol(trans)

trade = Trade()

struct_obj = proto.readStructBegin()


while True:
    id = 2
    field = proto.readFieldBegin()
    if field[id] == Thrift.TType.STOP:
        break
    if field[id] == 1:
        trade.symbol = proto.readString()
    elif field[id] == 2:
        trade.price = proto.readDouble()
    elif field[id] == 3:
        trade.size = proto.readI32()
    else:
        proto.skip(field[1])
    proto.readFieldEnd()

proto.readStructEnd()
        
print("Wrote Trade: %s %d @ %f" % 
      (trade.symbol, trade.size, trade.price))

