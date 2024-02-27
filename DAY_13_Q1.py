# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_element = nums[0]
        for i in range(len(nums)):
            if(nums[i]<min_element):
                min_element = nums[i]
        return min_element
        
