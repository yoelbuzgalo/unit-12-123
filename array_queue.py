import arrays

class Queue:
    __slots__ = ['__elements','__front', '__back','__size']
    def __init__(self):
        self.__elements = arrays.Array(3)
        self.__front = 0
        self.__back = 0
        self.__size = 0

    def is_empty(self):
        if self.__size == 0:
            return True
        
    def __len__(self):
        return self.__size

    def __str__(self):
        stringify = ""
        for i in range(self.__front, self.__back):
            stringify += str(self.__elements[i]) + ", "
        return "["+ stringify[:-2] + "]"
    
    def enqueue(self, value):
        self.__elements[self.__back] = value
        self.__back = (self.__back + 1) % len(self.__elements)
        self.__size += 1

    def front(self):
        if self.__size == 0:
            raise IndexError("Empty Queue")
        return self.__elements[self.__front]

    def dequeue(self):
        if self.__size == 0:
            raise IndexError("Empty queue")
        value = self.__elements[self.__front]
        self.__elements[self.__front] = None
        self.__front = (self.__front+1) % len(self.__elements)
        self.__size -= 1
        return value