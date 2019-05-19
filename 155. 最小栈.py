class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.stack.append(x)
        if not self.minstack or x < self.minstack[-1]:
            self.minstack.append(x)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self):
        """
        :rtype: None
        """
        self.minstack.pop()

        self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()