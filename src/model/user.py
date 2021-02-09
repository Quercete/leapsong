import dataclasses
from typing import List


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
        # TODO: Save to firebase
        pass

    @staticmethod
    def load(key_id: str):
        # TODO: load from firebase
        pass

