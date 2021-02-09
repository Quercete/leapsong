from src.factory.abst.key_factory import AbstKeyFactory
from src.factory.abst.user_factory import AbstUserFactory


class KeyController:
    def __init__(self, key_factory: AbstKeyFactory, user_factory: AbstUserFactory):
        self.key_factory: AbstKeyFactory = key_factory
        self.user_factory: AbstUserFactory = user_factory

    def register_key(self, key_armor: str, discord_user_id: int):
        key = self.key_factory.create(key_armor)
        self.user_factory.add_key(discord_user_id, key.key_id)

    def get_key_from_user(self, discord_user_id: int):
        return self.key_factory.get_by_registered_user(discord_user_id)

    def get_key_from_id(self, key_id: str):
        return self.key_factory.get_by_key_id(key_id)

