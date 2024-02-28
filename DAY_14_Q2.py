# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merging the nums1 and nums2 to a new list as nums3
        nums3 = nums1 + nums2

        # Sorting the nums3 list
        nums3.sort()

        length = len(nums3)
        
        if(length%2==1):
            # If the total number of elements is odd then return the middle element.
            return (nums3[length//2])
        
        else:
            # If the total number of elements is even then we need to return the average of two middle elements as the median.
            med1 = nums3[length//2 - 1]
            med2 = nums3[length//2]

            return (med1+med2)/2.0

