import abc
from typing import List

from src.model.key import Key


class AbstKeyFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self, key_armor: str) -> Key:
        pass

    @abc.abstractmethod
    def get_by_registered_user(self, discord_user_id: int) -> List[Key]:
        pass

    @abc.abstractmethod
    def get_by_key_id(self, key_id: str) -> Key:
        pass
