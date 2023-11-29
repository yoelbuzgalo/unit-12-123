from node import Node

class Stack:
    __slots__ = ['__top']
    def __init__(self):
        self.__top = None

    def is_empty(self):
        if self.__top == None:
            return True
        return False
    
    def __stringify__(self, node, string=""):
        # Return all the values in the tack as a comma seperated string
        if node is None:
            return string
        else:
            string += str(node.get_value()) + ", "
            return Stack.__stringify__(node.get_next(), string)
        
    def __str__(self):
        return "[" + Stack.__stringify__(self.__top) + "]"