from abc import ABC, abstractmethod
from typing import List


class TouristSpot:
    """
    Implementation of a tourist spot
    """
    pass


class IAggregate(ABC):

    @abstractmethod
    def get_tourists_discretion_iterator(self) -> 'IIterator':
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def get_item(self, index: int) -> TouristSpot:
        pass


class IIterator(ABC):

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def current_item(self) -> TouristSpot:
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass


class TouristSpotCollectionAggregate(IAggregate):
    def __init__(self, spots: List[TouristSpot]):
        self.array = spots

    def append(self, item: TouristSpot):
        self.array.append(item)

    def remove(self, index: int):
        del self.array[index]

    def get_tourists_discretion_iterator(self) -> 'IIterator':
        return TouristsDiscretionIterator(self)

    def get_navigator_recommendation_iterator(self) -> 'IIterator':
        return NavigatorRecommendationIterator(self)

    def get_local_guide_iterator(self) -> 'IIterator':
        return LocalGuideIterator(self)

    def count(self) -> int:
        return len(self.array)

    def get_item(self, index: int) -> TouristSpot:
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise ValueError("Error. Bad index")


class IteratorBase(IIterator):
    def __init__(self, collection: IAggregate):
        self.aggregate = collection
        self.current = 0

    def first(self):
        self.current = 0

    def next(self):
        self.current += 1

    def current_item(self) -> TouristSpot:
        if not self.is_done():
            return self.aggregate.get_item(self.current)
        else:
            raise ValueError("Error")

    def is_done(self) -> bool:
        return self.current >= self.aggregate.count()


class TouristsDiscretionIterator(IteratorBase):
    def __init__(self, collection: IAggregate):
        super().__init__(collection)

    def next(self):
        super().next()
        # Implementation for tourist's discretion


class NavigatorRecommendationIterator(IteratorBase):
    def __init__(self, collection: IAggregate):
        super().__init__(collection)

    def next(self):
        super().next()
        # Implementation for navigator recommendations


class LocalGuideIterator(IteratorBase):
    def __init__(self, collection: IAggregate):
        super().__init__(collection)

    def next(self):
        super().next()
        # Implementation for local guide


spots = [TouristSpot() for _ in range(10)]
collection = TouristSpotCollectionAggregate(spots)

tourists_discretion_iterator = collection.get_tourists_discretion_iterator()
navigator_recommendation_iterator = collection.get_navigator_recommendation_iterator()
local_guide_iterator = collection.get_local_guide_iterator()

# Example usage
tourists_discretion_iterator.first()
while not tourists_discretion_iterator.is_done():
    tourists_discretion_iterator.next()