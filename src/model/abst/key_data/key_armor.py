import abc
import dataclasses

@dataclasses.dataclass
class KeyArmor(metaclass=abc.ABCMeta):
    key_armor: str


