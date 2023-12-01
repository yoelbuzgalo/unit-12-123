import arrays

class Queue:
    __slots__ = ['__elements','__front', '__back','__size']
    def __init__(self):
        self.__elements = arrays.Array(3)
        self.__front = 0
        self.__back = 0
        self.__size = 0
