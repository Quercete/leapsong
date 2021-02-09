import dataclasses
import pgpy
from pgpy.constants import KeyFlags

from .key_data.user_id import KeyUserId
from .key_data.usage import Usage


@dataclasses.dataclass
class Key:
    key_armor: str
    key_id: str
    fingerprint: str
    key_user_id: KeyUserId
    usage: Usage

    @staticmethod
    def from_key_armor(key_armor: str):
        try:
            parsed_key = pgpy.PGPKey.from_blob(key_armor.replace("\\n", "\n"))
            key: pgpy.PGPKey = parsed_key[0]
            long_key_id = list(parsed_key[1].keys())[0][0]
        except ValueError:
            return None

        return Key(
            key_armor=key_armor,
            key_id=long_key_id,
            fingerprint=key.fingerprint.replace(" ", ""),
            key_user_id=KeyUserId(
                name=key.userids[0].name,
                email=key.userids[0].email,
                comment=key.userids[0].comment,
            ),
            usage=Usage(
                for_authenticate=KeyFlags.Authentication in key._get_key_flags(),
                for_certify=KeyFlags.Certify in key._get_key_flags(),
                for_encrypt=KeyFlags.EncryptStorage in key._get_key_flags()
                            and KeyFlags.EncryptCommunications in key._get_key_flags(),
                for_sign=KeyFlags.Sign in key._get_key_flags()
            )
        )

    def to_dict(self) -> dict:
        return {
            "key_armor": self.key_armor,
            "key_id": self.key_id,
            "fingerprint": self.fingerprint,
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

    @staticmethod
    def from_dict(data_dict: dict):
        return Key(
            key_armor=data_dict["key_armor"],
            key_id=data_dict["key_id"],
            fingerprint=data_dict["fingerprint"],
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

    def save(self):
        # TODO: Save to firebase
        pass

    @staticmethod
    def load(key_id: str):
        # TODO: load from firebase
        pass

