from node import Node

class Stack:
    __slots__ = ['__top', '__size']
    def __init__(self):
        self.__top = None
        self.__size = 0

    def is_empty(self):
        if self.__top == None:
            return True
        return False
    
    def __stringify(node, string=""):
        # Return all the values in the stack as a comma seperated string
        if node == None:
            return string
        else:
            string += str(node.get_value()) + ", "
            return Stack.__stringify(node.get_next(), string)
        
    def __str__(self):
        return "[" + Stack.__stringify(self.__top)[:-2] + "]"
    
    def __len__(self):
        return self.__size
    
    def peek(self):
        if self.__top == None:
            raise IndexError("Can't peek an empty queue")
        return self.__top.get_value()
    
    def pop(self):
        if self.__top == None:
            raise IndexError("Cant pop an empty queue")
        value = self.__top.get_value()
        self.__top = self.__top.get_next()
        self.__size -= 1
        
        return value

    def push(self, value):
        new_node = Node(value)
        new_node.set_next(self.__top)
        self.__top = new_node
        self.__size += 1