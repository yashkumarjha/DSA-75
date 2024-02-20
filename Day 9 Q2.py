# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # As mentioned in the question that we have numbers list in sorted non-decreasing order means sorted ascending order 
        # So we'll take left as 0 and right as the last index of the list.
        # And we'll try to iterate till we get numbers[left]+numbers[right]=target.
        left = 0
        right = len(numbers)-1

        while(numbers[left]+numbers[right]!=target):
            # If the sum of numbers[left] and numbers[right] is greater than target that means the number should be 
            # smaller and should be in left side as this is a sorted ascending order list.
            if(numbers[left]+numbers[right]>target):
                right = right-1
            # if the sum of numbers[left] and numbers[right] is less than the target that means the number should be 
            # greater and should be in the right side as this is a sorted ascending order list.
            else:
                left=left+1
        # At the end when we have the correct left and right that means when we get numbers[left] + numbers[right] = target then that time it'll exit from the loop.
        # And we're left with left and right based on index and we need to increment 1 in index to get the actual position.
        return (left+1,right+1)
