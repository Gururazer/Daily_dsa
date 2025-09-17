import collections
import heapq
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        
        self.food_to_rating = {}
        
        self.food_to_cuisine = {}
        
        self.cuisine_to_pq = collections.defaultdict(list)

        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            
            self.food_to_rating[food] = rating
            self.food_to_cuisine[food] = cuisine
            
            
            heapq.heappush(self.cuisine_to_pq[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
      
        self.food_to_rating[food] = newRating
        
       
        cuisine = self.food_to_cuisine[food]
        
       
        heapq.heappush(self.cuisine_to_pq[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
       
        pq = self.cuisine_to_pq[cuisine]
        
       
        while True:
       
            neg_rating, food = pq[0]
            current_rating = self.food_to_rating[food]
            
       
            if -neg_rating == current_rating:
                return food
            else:
       
                heapq.heappop(pq)