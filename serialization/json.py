import flatbuffers
from zenoh import Encoding, Value
from .Timescales import Message
from .Timescales.NullableBool import *
from .Timescales.NullableInt64 import *
from rosbags.serde import *


def encode_json(data, with_time=True):
    if not with_time:
        message = Value(data[1], Encoding.TEXT_JSON)
    else:
        message = Value(data, Encoding.TEXT_JSON)

    return message


     
        

    
