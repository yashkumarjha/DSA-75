# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        deque = collections.deque([('(',1,0)])
        while deque:
            curr, left, right = deque.popleft()
            if(left>=right and left<=n and right<=n):
                if(len(curr)==n*2):
                    result.append(curr)
                deque.append((curr+"(",left+1, right))
                deque.append((curr+')',left, right+1))
        return result        
