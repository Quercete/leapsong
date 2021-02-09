import dataclasses

@dataclasses.dataclass
class User:
    discord_user_id: int
    cached_discord_username: str

    def to_dict(self) -> dict:
        return {
            "discord_user_id": self.discord_user_id,
            "cached_discord_username": self.cached_discord_username
        }

    @staticmethod
    def from_dict(data_dict):
        return User(
            discord_user_id=data_dict["discord_user_id"],
            cached_discord_username=data_dict["cached_discord_username"]
        )

