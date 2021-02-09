import dataclasses

@dataclasses.dataclass
class User:
    discord_user_id: int

    def to_dict(self) -> dict:
        return {
            "discord_user_id": self.discord_user_id,
        }

    @staticmethod
    def from_dict(data_dict):
        return User(
            discord_user_id=data_dict["discord_user_id"],
        )
