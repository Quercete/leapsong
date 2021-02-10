import dataclasses
from typing import List

from firebase_admin import db


@dataclasses.dataclass
class User:
    discord_user_id: int
    key_ids: List[str]

    def to_dict(self) -> dict:
        return {
            "discord_user_id": self.discord_user_id,
            "key_ids": self.key_ids
        }

    @staticmethod
    def from_dict(data_dict):
        return User(
            discord_user_id=data_dict["discord_user_id"],
            key_ids=data_dict["key_ids"]
        )

    def save(self):
        ref = db.reference("users").child(str(self.discord_user_id))
        ref.set(self.key_ids)

    # TODO: fetchとかの名前のほうが良くね
    @staticmethod
    def load(discord_user_id: int):
        ref = db.reference("users").child(str(discord_user_id))
        key_ids = ref.get()

        user = User(
            discord_user_id=discord_user_id,
            key_ids=list(key_ids)
        )

        return user
