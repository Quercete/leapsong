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


    def to_dict(self) -> dict:
        return {
            "key_armor": self.key_armor.key_armor,
            "user_id": {
                "name": self.user_id.name,
                "email": self.user_id.email,
                "comment": self.user_id.comment
            },
            "usage": {
                "auth": self.usage.for_authenticate,
                "cert": self.usage.for_certify,
                "enc": self.usage.for_encrypt,
                "sign": self.usage.for_sign
            }
        }

    def from_dict(data_dict: dict):
        return Key(
            key_armor=data_dict["key_armor"],
            user_id=UserId(
                name=data_dict["user_id"]["name"],
                email=data_dict["user_id"]["email"],
                comment=data_dict["user_id"]["comment"],
            ),
            usage=Usage(
                for_authenticate=data_dict["usage"]["auth"],
                for_certify=data_dict["usage"]["cert"],
                for_encrypt=data_dict["usage"]["enc"],
                for_sign=data_dict["usage"]["sign"]
            )
        )

