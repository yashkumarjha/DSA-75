# https://leetcode.com/problems/min-stack/description/
# Retrieving the minimum element in constant time.

class MinStack:
    # Initializing of 2 stacks as stack and stack_desc.
    def __init__(self):
        self.stack = []
        self.stack_desc = []
      
    # Appending val to stack.
    # Appending val to stack only if it's less than or equal to the minimum element.
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack_desc or val <= self.stack_desc[-1]:
            self.stack_desc.append(val)
    
    # Pop the top element from stack    
    # Pop the top element from stack desc if top elements match.
    def pop(self) -> None:
        if self.stack.pop() == self.stack_desc[-1]:
            self.stack_desc.pop()
    
    # This will give the top element of stack.
    def top(self) -> int:
        return self.stack[-1]
      
    # This will retun the top element of stack_desc which is the minimum element.
    def getMin(self) -> int:
        return self.stack_desc[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
