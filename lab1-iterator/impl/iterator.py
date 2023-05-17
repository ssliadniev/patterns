from api.spot import BaseTouristSpot
from api.iterator import BaseIterator
from api.aggregator import BaseAggregator


class Iterator(BaseIterator):
    """
    Implementation of class for an iterator
    """

    def __init__(self, aggregate: BaseAggregator):
        self.aggregate = aggregate
        self.current = 0

    def first(self):
        """
        Reset the iterator to the first item
        """
        self.current = 0

    def next(self):
        """
        Move the iterator to the next item
        """
        self.current += 1

    def current_item(self) -> BaseTouristSpot:
        """
        Get the current item in the collection
        """
        if not self.is_done():
            return self.aggregate.get_item(self.current)
        else:
            raise ValueError("Iterator out of bounds")

    def is_done(self) -> bool:
        """
        Check if the iterator has reached the end of the collection
        """
        return self.current >= self.aggregate.count()
