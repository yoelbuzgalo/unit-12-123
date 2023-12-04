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
        for i in range(self.__size):
            stringify += str(self.__elements[i]) + ", "
        return "["+ stringify[:-2] + "]"
    
    def __resize(self):
        new_elements = arrays.Array(self.__size*2)
        for i in range(self.__size):
            front = (self.__front + i) % self.__size
            new_elements[i] = self.__elements[front]
        self.__elements = new_elements
        self.__front = 0
        self.__back = self.__size
        
    
    def enqueue(self, value):
        if self.__size == len(self.__elements):
            self.__resize()
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