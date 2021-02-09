import abc

from src.model.User import User

class UserFactroy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self, discord_user_id: int) -> User:
        pass

    @abc.abstractmethod
    def add_key(self, discord_user_id: int, key_identify_id: int) -> User:
        pass

    @abc.abstractmethod
    def remove_key(self, discord_user_id: int, key_identify_id: int) -> User:
        pass

