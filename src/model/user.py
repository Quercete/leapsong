import dataclasses
from typing import List

@dataclasses.dataclass
class User:
    discord_user_id: int
    keys: List[int]

    def to_dict(self) -> dict:
        return {
            "discord_user_id": self.discord_user_id,
            "keys": self.keys
        }

    @staticmethod
    def from_dict(data_dict):
        return User(
            discord_user_id=data_dict["discord_user_id"],
            keys=data_dict["keys"]
        )

