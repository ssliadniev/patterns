from impl.iterator import Iterator
from impl.aggregator import BaseAggregator


class LocalGuideIterator(Iterator):
    """Iterator for a local guide"""

    def __init__(self, aggregate: BaseAggregator):
        super().__init__(aggregate)

    def next(self):
        super().next()
        # Implementation for local guide
