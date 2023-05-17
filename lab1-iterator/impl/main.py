from impl.spot import TouristSpot
from impl.aggregator import TouristSpotCollectionAggregate


spots = [TouristSpot() for _ in range(20)]
collection = TouristSpotCollectionAggregate(spots)

tourists_discretion_iterator = collection.get_tourists_discretion_iterator()
navigator_recommendation_iterator = collection.get_navigator_recommendation_iterator()
local_guide_iterator = collection.get_local_guide_iterator()


tourists_discretion_iterator.first()
while not tourists_discretion_iterator.is_done():
    tourists_discretion_iterator.next()
