from pycdr2 import IdlStruct
from dataclasses import dataclass
from pycdr2.types import int64, int8
from pycdr2 import Optional

@dataclass
class NullableInt64(IdlStruct):
    val: int64

@dataclass 
class NullableBool(IdlStruct):
    val: int8

@dataclass
class Message(IdlStruct):
    time: NullableInt64
    p: NullableBool
    q: NullableBool
    r: NullableBool
    s: NullableBool


def serialize(data, with_time=True, persistent=False):
    data_dict = data.data._asdict()
        
    
    



