# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Looping in the outer list to get the number of inner list.
        for i in range(len(matrix)):  
            # Looping individually in the inner list
            for j in range(len(matrix[i])):
                # Checking if the inner list contains target
                if(matrix[i][j]==target):
                    # If yes, then return True
                    return True
        # After the loop is over means there is not the presence of target variables in the whole inner and outer list and in the whole matrix. Then we'll return false.
        return False
