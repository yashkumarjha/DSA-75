# https://leetcode.com/problems/car-fleet/description/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stk = []

        # Created pairs of position and speed for each car.
        for i in range(len(speed)):
            pairs.append([position[i], speed[i]])
        
        # To sort the pairs based on the position in descending order
        pairs = sorted(pairs)[::-1]

        # Iterate through the sorted pairs 
        for i,v in pairs:
            # We need to calculate the time to reach the target for the current car
            time = (target - i)/v

            # Add the time to the empty stack we've initialized earlier.
            stk.append(time)

            # To check if there're at least 2 cars in the stack and the current car
            # takes less or equal time than the previous car and if yes then we'll pop the previous car
            if(len(stk)>=2 and stk[-1]<=stk[-2]):
                stk.pop()
            
        # Return the length of stack which represents the number of car fleets.
        return len(stk)
        
