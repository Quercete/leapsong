import dataclasses

from firebase_admin import db
from firebase_admin import storage

from .key_data.user_id import KeyUserId
from .key_data.usage import Usage


@dataclasses.dataclass
class Key:
    key_id: str
    key_armor: str
    key_armor_url: str
    key_user_id: KeyUserId
    usage: Usage

    def to_dict(self) -> dict:
        return {
                "key_id": self.key_id,
                "key_armor": self.key_armor,
                "key_armor_url": self.key_armor_url,
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
        if "key_armor_url" in data_dict.keys():
            key_armor_url = data_dict["key_armor_url"]
        else:
            key_armor_url = Key.__upload_key_armor(data_dict["key_id"], data_dict["key_armor"])

        return Key(
            key_id=data_dict["key_id"],
            key_armor=data_dict["key_armor"],
            key_armor_url=key_armor_url,
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
        data = self.to_dict()
        data.pop("key_id")
        data.pop("armor")

        db_ref = db.reference("keys").child(self.key_id)
        db_ref.set(data)

        Key.__upload_key_armor(self.key_id, self.key_armor)

    # TODO: fetchとかの名前のほうが良くね
    @staticmethod
    def load(key_id: str):
        db_ref = db.reference("keys").child(key_id)

        data = db_ref.get()
        data["key_id"] = key_id
        data["key_armor"] = Key.__fetch_key_armor_from_key_id(key_id)

        key = Key.from_dict(data)
        return key

    @staticmethod
    def __upload_key_armor(key_id: str, key_armor: str) -> str:
        bucket = storage.bucket()
        blob = bucket.blob(key_id)

        blob.upload_from_string(key_armor)

        if key_id not in bucket.list_blobs():
            raise RuntimeError("Could not save the key_armor of the key id: {}", key_id)

        return blob.self_link

    @staticmethod
    def __fetch_key_armor_from_key_id(key_id: str) -> str:
        bucket = storage.bucket()
        blob = bucket.blob(key_id)

        raw_bytes = blob.download_as_bytes()
        data = raw_bytes.decode(encoding="UTF-8")

        return data

    def __fetch_key_armor(self) -> str:
        data = Key.__fetch_key_armor_from_key_id(self.key_id)
        return data
