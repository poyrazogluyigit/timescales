import zenoh

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from serialization.flatbuf import Flatbuffers

def listener(sample):
    # print(sample.payload)
    decoded_message = Flatbuffers.decode_flatbuf(sample.payload)
    print(decoded_message)

session = zenoh.open()
sub = session.declare_subscriber('timescales', listener)