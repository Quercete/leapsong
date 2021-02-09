import abc

from src.model.key import Key

class KeyFactroy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self, key_armor: str) -> Key:
        pass

    @abc.abstractmethod
    def get_by_registered_user(self, discord_user_id: int) -> Key:
        pass

    @abc.abstractmethod
    def get_by_identify_id(self, identify_id: int) -> Key:
        pass

