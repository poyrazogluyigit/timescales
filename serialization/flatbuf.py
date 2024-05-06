import flatbuffers
from .Timescales import Message

class Flatbuffers:

    # builder = flatbuffers.Builder(512)

    @classmethod
    def encode_flatbuf(self, data, with_time=True, persistent=False, previous=None):

        from .Timescales.NullableBool import CreateNullableBool
        from .Timescales.NullableInt64 import CreateNullableInt64

        # builder = Flatbuffers.builder
        builder = flatbuffers.Builder(512)
        Message.MessageStart(builder)

        if (with_time):
            Message.MessageAddTime(builder, CreateNullableInt64(builder, data.time))
        
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
        builder.Finish(msg)
        buf = builder.Output()
        return bytes(buf)


    @classmethod
    def decode_flatbuf(self, message):
        msg_bytearray = bytearray(message)
        msg = Message.Message.GetRootAsMessage(msg_bytearray, 0)
        dec_msg = dict()

        if msg.Time():
            dec_msg['time'] = msg.Time().Value()
        
        if msg.PropP():
            dec_msg['p'] = msg.PropP().Value()

        if msg.PropQ():
            dec_msg['q'] = msg.PropQ().Value()
        
        if msg.PropR():
            dec_msg['r'] = msg.PropR().Value()

        if msg.PropS():
            dec_msg['s'] = msg.PropS().Value()

        return dec_msg




if __name__ == "__main__":
    import sys
    # for msg in flatbuf_reader(sys.argv[1]):
    #    print(msg)
