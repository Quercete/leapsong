import abc
import dataclasses

@dataclasses.dataclass
class UserId(metaclass=abc.ABCMeta):
    name: str
    email: str
    comment: str

