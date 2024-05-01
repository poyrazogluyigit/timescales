import zenoh
from serialization.flatbuf import Flatbuffers

def listener(sample):
    decoded_message = Flatbuffers.decode_flatbuf(sample.payload)
    print(decoded_message)

session = zenoh.open()
sub = session.declare_subscriber('timescales', listener)