from api.aggregator import BaseAggregator
from api.iterator import BaseIterator
from api.spot import BaseTouristSpot

from impl.tourists_discretion_iterator import TouristsDiscretionIterator
from impl.navigator_recommendation_iterator import NavigatorRecommendationIterator
from impl.local_guide_iterator import LocalGuideIterator

from typing import List


class TouristSpotCollectionAggregate(BaseAggregator):

    def __init__(self, spots: List[BaseTouristSpot]):
        self.array = spots

    def append(self, item: BaseTouristSpot):
        self.array.append(item)

    def remove(self, index: int):
        del self.array[index]

    def get_tourists_discretion_iterator(self) -> BaseIterator:
        return TouristsDiscretionIterator(self)

    def get_navigator_recommendation_iterator(self) -> BaseIterator:
        return NavigatorRecommendationIterator(self)

    def get_local_guide_iterator(self) -> BaseIterator:
        return LocalGuideIterator(self)

    def count(self) -> int:
        return len(self.array)

    def get_item(self, index: int) -> BaseTouristSpot:
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise ValueError("Error. Bad index")
