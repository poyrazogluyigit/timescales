import zenoh
from zenoh import Encoding

def listener(sample):
    print(f"Output: {sample.payload.decode()}")


session = zenoh.open()
sub = session.declare_subscriber('timescales', listener)
