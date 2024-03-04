# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Initializing left with 0 and right with the length of the first string
        left = 0
        right = len(s1)
        
        # We are using this counter just to compare it's anagram of this with s2 
        countS1 = collections.Counter(s1)

        # implementing a while loop and it'll iterate till the point length of s3 will be equal to length of s2
        while(right<=len(s2)):
            # Comparing the anagram of it with s2.
            if(countS1==collections.Counter(s2[left:right])):
                # if this condition is true then return true otherwise increment both left and right with 1 and carry on in this loop till len(s1) = len(s2)
                return True
            left = left+1
            right = right+1
        # If anything till this point won't come as output then definitely it's not the solution and we need to return False.
        return False
