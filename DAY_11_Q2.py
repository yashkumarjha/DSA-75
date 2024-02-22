# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        mid = (left+right)//2
        if(target in nums):
            while(left<right):           
                if(nums[mid]==target):
                    return mid
                elif(nums[mid]>target):
                    right = mid-1
                    mid = (left+right)//2
                elif(nums[mid]<target):
                    left = mid+1
                    mid = (left+right)//2
        else: 
            return -1
        return mid

        
