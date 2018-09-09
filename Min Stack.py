class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minstack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.minstack.insert(0, x)
        else:
            if x<=self.minstack[0]:
                self.minstack.insert(0, x)
        self.stack.insert(0, x)

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop(0)
        if x == self.minstack[0]:
            self.minstack.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
