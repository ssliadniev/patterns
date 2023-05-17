from impl.iterator import Iterator
from impl.aggregator import BaseAggregator


class TouristsDiscretionIterator(Iterator):
    """Iterator for tourist's discretion"""

    def __init__(self, aggregate: BaseAggregator):
        super().__init__(aggregate)

    def next(self):
        super().next()
        # Implementation for tourist's discretion
