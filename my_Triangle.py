# 3.4.1.15 Triangle
# new class will be called Triangle and this is the list of our expectations:

# the constructor accepts three arguments - all of them are objects of the Point class;
# the points are stored inside the object as a private list;
# the class provides a parameterless method called perimeter(),
# which calculates the perimeter of the triangle described by the three points;

from math import hypot


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        if x > self.__x:
            hx = x - self.__x
        else:
            hx = self.__x - x
        if y > self.__y:
            hy = y - self.__y
        else:
            hy = self.__y - y
        return hypot(hx, hy)

    def distance_from_point(self, point):
        px = point.getx()
        py = point.gety()
        return self.distance_from_xy(px, py)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertice1 = vertice1
        self.__vertice2 = vertice2
        self.__vertice3 = vertice3

    def perimeter(self):
        s1 = self.__vertice1.distance_from_point(self.__vertice2)
        s2 = self.__vertice2.distance_from_point(self.__vertice3)
        s3 = self.__vertice3.distance_from_point(self.__vertice1)
        return s1 + s2 + s3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())  # 3.414213562373095
