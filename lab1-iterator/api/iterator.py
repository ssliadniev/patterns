from abc import ABC, abstractmethod

from api.spot import BaseTouristSpot


class BaseIterator(ABC):
    """
    Base class for an iterator
    """

    @abstractmethod
    def first(self):
        """
        Reset the iterator to the first item
        """
        pass

    @abstractmethod
    def next(self):
        """
        Move the iterator to the next item
        """
        pass

    @abstractmethod
    def current_item(self) -> BaseTouristSpot:
        """
        Get the current item in the collection
        """
        pass

    @abstractmethod
    def is_done(self) -> bool:
        """
        Check if the iterator has reached the end of the collection
        """
        pass
