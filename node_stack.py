class Stack:
    __slots__ = ['__top']
    def __init__(self):
        self.__top = None

    def is_empty(self):
        if self.__top == None:
            return True
        return False
    