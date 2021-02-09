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
        update_object: dict = {
            self.discord_user_id: {
                self.key_ids
            }
        }

        ref = db.reference("users")
        ref.set(update_object)

    # TODO: fetchとかの名前のほうが良くね
    @staticmethod
    def load(discord_user_id: str):
        ref = db.reference("users").child(discord_user_id)

        data = ref.get()
        user = User.from_dict(data)
        return user
