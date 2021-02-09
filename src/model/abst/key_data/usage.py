import abc
import dataclasses

@dataclasses.dataclass
class Usage(metaclass=abc.ABCMeta):
    for_authenticate: bool
    for_certify: bool
    for_encrypt: bool
    for_sign: bool
