from abc import ABC, abstractmethod

from api.iterator import BaseIterator
from api.spot import BaseTouristSpot


class BaseAggregator(ABC):

    @abstractmethod
    def get_tourists_discretion_iterator(self) -> BaseIterator:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def get_item(self, index: int) -> BaseTouristSpot:
        pass
