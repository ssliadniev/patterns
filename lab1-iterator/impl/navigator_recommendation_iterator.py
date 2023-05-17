from impl.iterator import Iterator
from impl.aggregator import BaseAggregator


class NavigatorRecommendationIterator(Iterator):
    """Iterator for navigator recommendations"""

    def __init__(self, aggregate: BaseAggregator):
        super().__init__(aggregate)

    def next(self):
        super().next()
        # Implementation for navigator recommendation
