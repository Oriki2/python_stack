from stack import Stack


class UpgradedStack(Stack):
    def __init__(self):
        super(Stack, self).__init__()
        self.items = []
        self.__max_stack = Stack()

    def max_val(self):

        return self.__max_stack.peek()


    def push(self, item):

        if self.__max_stack.is_empty():
            self.__max_stack.push(item)
        elif item>= self.__max_stack.peek():
            self.__max_stack.push(item)
        super(UpgradedStack,self).push(item)

    def pop(self):
        if super(UpgradedStack,self).peek()==self.__max_stack.peek():
            a=self.__max_stack.pop()
            super(UpgradedStack,self).pop()
            return a

        else:
            a=super(UpgradedStack,self).pop()
            return  a
