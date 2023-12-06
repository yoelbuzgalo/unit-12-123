class Stack:
    __slots__ = ['__list', '__size']
    def __init__(self):
        self.__list = []
        self.__size = 0

    def is_empty(self):
        if len(self.__list) == 0:
            return True
        return False
        
    def __str__(self):
        return str(self.__list)
    
    def __len__(self):
        return self.__size
    
    def peek(self):
        if self.__list[-1] == None:
            raise IndexError("Can't peek an empty queue")
        return self.__list[-1]
    
    def pop(self):
        if self.__list[0] == None:
            raise IndexError("Cant pop an empty queue")
        self.__size -= 1
        return self.__list.pop()

    def push(self, value):
        self.__list.append(value)
        self.__size += 1