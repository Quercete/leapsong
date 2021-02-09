import abc
import dataclasses
from .key_data.key_armor import KeyArmor
from .key_data.user_id import UserId
from .key_data.usage import Usage

@dataclasses.dataclass
class Key(metaclass=abc.ABCMeta):
    key_armor: KeyArmor
    user_id: UserId
    usage: Usage

