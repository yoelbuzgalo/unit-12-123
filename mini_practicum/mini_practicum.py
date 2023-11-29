class Circle:
    __slots__ = ['__center', '__radius']
    

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
    
