# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i not in "+-*/":
                stk.append(int(i))
            else:
                r = stk.pop()
                l = stk.pop()
                if(i=="+"):
                    stk.append(l+r)
                elif(i=="-"):
                    stk.append(l-r)
                elif(i=="*"):
                    stk.append(l*r)
                else:
                    stk.append(int(float(l)/r))
        return stk.pop()
