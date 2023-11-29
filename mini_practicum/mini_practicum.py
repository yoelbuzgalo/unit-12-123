import math

class Circle:
    __slots__ = ['__center', '__radius']
    def __init__(self, center, radius):
        self.__center = center
        self.__radius = radius

    def __repr__(self):
        return "center: " + "("+str(self.__center[0])+", "+str(self.__center[1])+")"\
        +" radius: "+ str(self.__radius)\
    
    def __lt__(self, other):
        if type(self) == type(other):
            if self.__radius < other.__radius:
                return True
        return False
    
    def get_center(self):
        return self.__center
    
    def get_radius(self):
        return self.__radius
    
    def intersect(self, circle):
        sum_radii = self.__radius + circle.get_radius()
        x1 = self.__center[0]
        x2 = circle.get_center()[0]
        y1 = self.__center[1]
        y2 = circle.get_center()[1]
        distance_centers = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        
        if sum_radii > distance_centers:
            return True
        
        return False
    

def main():
    circle1 = Circle((0, 0), 2)
    circle2 = Circle((4, 0), 3) 
    circle3 = Circle((3, 3), 1)
    a_list = [circle1, circle2, circle3]
    a_list.sort()
    print(a_list)
    print("circle1 and circle2 intersect:", circle1.intersect(circle2)) # True
    print("circle1 and circle3 intersect:", circle1.intersect(circle3)) # False
    print("circle2 and circle3 intersect:", circle2.intersect(circle3)) # True

main()           
    
