class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
                
        total_drunk = numBottles
        empty_bottles = numBottles    
        
        while empty_bottles >= numExchange:
            
            empty_bottles_used = numExchange
                        
            new_full_bottle = 1
                        
            empty_bottles -= empty_bottles_used
                        
            numExchange += 1
                        
            total_drunk += new_full_bottle            
            
            empty_bottles += new_full_bottle
            
        return total_drunk

