import flatbuffers
from zenoh import Encoding, Value
from .Timescales import Message
from .Timescales.NullableBool import *
from .Timescales.NullableInt64 import *
from rosbags.serde import *


def encode_flatbuf(data, with_time=True, persistent=False, previous=None):
    builder = flatbuffers.Builder(256)

    if (with_time):
        Message.MessageAddTime(builder, CreateNullableBool(builder, data.time))
    
    if not persistent:
        input_data = data.data._asdict()
        if 'p' in input_data:
            Message.MessageAddPropP(builder, CreateNullableBool(builder, input_data['p']))
        if 'q' in input_data:
            Message.MessageAddPropQ(builder, CreateNullableBool(builder, input_data['q']))
        if 'r' in input_data:
            Message.MessageAddPropR(builder, CreateNullableBool(builder, input_data['r']))
        if 's' in input_data:
            Message.MessageAddPropS(builder, CreateNullableBool(builder, input_data['s']))

    else:
        if (previous is None):
            raise ValueError('Persistent Encoding - Previous cannot be of type None.')
        current = data.data._asdict()
        previous = previous.data._asdict()
        if 'p' in current and (not 'p' in previous or current['p'] != previous['p']):
                    Message.MessageAddPropP(
                        builder, CreateNullableBool(builder, current['p']))
        if 'q' in current and (not 'q' in previous or current['q'] != previous['q']):
            Message.MessageAddPropQ(
                builder, CreateNullableBool(builder, current['q']))
        if 'r' in current and (not 'r' in previous or current['r'] != previous['r']):
            Message.MessageAddPropR(
                builder, CreateNullableBool(builder, current['r']))
        if 's' in current and (not 's' in previous or current['s'] != previous['s']):
            Message.MessageAddPropS(
                builder, CreateNullableBool(builder, current['s']))



    msg = Message.MessageEnd(builder)
    builder.FinishSizePrefixed(msg)
    buf = builder.Output()
    return buf


def encode_json(data, with_time=True):
    if not with_time:
        message = Value(data[1], Encoding.TEXT_JSON)
    else:
        message = Value(data, Encoding.TEXT_JSON)

    return message


     
        

    
