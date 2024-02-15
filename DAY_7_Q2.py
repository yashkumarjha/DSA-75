# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Solving this problem using stack approach because in that we can't change the order of temperature
        
        # Initializing an empty stack.
        stack = []

        # Initializing result with all the elements set to 0
        result = [0]*len(temperatures)

        # Iterating through all the temperatures list using for loop.
        for i in range(len(temperatures)):
            # using while loop till the stack is not empty and the temperature of current day is greater than the temperature of the day represented by the index at the top of the stack.
            while(stack and temperatures[i]>temperatures[stack[-1]]):
                # If the above condition satisfied then we pop the index from the stack and calculate the number of days until we get the next warmer day by subtracting current index from popped index.
                index = stack.pop()
                result[index] = i - index
            # Appending the current index to the stack
            stack.append(i)
        # Return the result list containing the number of days until we get the next warmer temperature for each day.
        return result
        
