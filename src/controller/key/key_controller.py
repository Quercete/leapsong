from src.model.key import Key
from src.model.user import User


class KeyController:
    def register_key(self, key_armor: str, discord_user_id: int):
        key = Key.from_key_armor(key_armor)
        user = User.load(discord_user_id)
        user.key_ids.append(key.key_id)
        key.save()
        user.save()

    def get_key_from_user(self, discord_user_id: int):
        user = User.load(discord_user_id)
        return [self.get_key_from_id(x) for x in user.key_ids]

    def get_key_from_id(self, key_id: str):
        return Key.load(key_id)
