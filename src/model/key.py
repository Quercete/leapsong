import dataclasses
from .key_data.user_id import KeyUserId
from .key_data.usage import Usage


@dataclasses.dataclass
class Key:
    key_armor: str
    key_user_id: KeyUserId
    usage: Usage

    def to_dict(self) -> dict:
        return {
            "key_armor": self.key_armor,
            "key_user_id": {
                "name": self.key_user_id.name,
                "email": self.key_user_id.email,
                "comment": self.key_user_id.comment
            },
            "usage": {
                "auth": self.usage.for_authenticate,
                "cert": self.usage.for_certify,
                "enc": self.usage.for_encrypt,
                "sign": self.usage.for_sign
            }
        }

    def from_dict(self, data_dict: dict):
        return Key(
            key_armor=data_dict["key_armor"],
            key_user_id=KeyUserId(
                name=data_dict["key_user_id"]["name"],
                email=data_dict["key_user_id"]["email"],
                comment=data_dict["key_user_id"]["comment"],
            ),
            usage=Usage(
                for_authenticate=data_dict["usage"]["auth"],
                for_certify=data_dict["usage"]["cert"],
                for_encrypt=data_dict["usage"]["enc"],
                for_sign=data_dict["usage"]["sign"]
            )
        )
