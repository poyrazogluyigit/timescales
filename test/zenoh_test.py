import zenoh

def listener(sample):
    print(f"{sample.payload.decode('utf-8')}")


session = zenoh.open()
sub = session.declare_subscriber('timescales', listener)
