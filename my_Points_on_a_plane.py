# Each point located on the plane can be described as a pair of coordinates customarily called x and y.
# write a Python class which stores both coordinates as float numbers.
# we want the objects of this class to evaluate the distances between any of the two points situated on the plane.

# employ the function named hypot() (available through the math module)
# which evaluates the length of the hypotenuse of a right triangle

# Class is called Point;
# its constructor accepts two arguments (x and y respectively), both default to zero;
# all the properties should be private;
# the class contains two parameterless methods called getx() and gety(),
# which return each of the two coordinates (the coordinates are stored privately,
# so they cannot be accessed directly from within the object);

# the class provides a method called distance_from_xy(x,y),
# which calculates and returns the distance between the point
# stored inside the object and the other point given as a pair of floats;

# the class provides a method called distance_from_point(point),
# which calculates the distance (like the previous method),
# but the other point's location is given as another Point class object;

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


point1 = Point(0, 0)
point2 = Point(1, 1)

print(point1.distance_from_point(point2))     # 1.4142135623730951
print(point2.distance_from_xy(2, 0))    # 1.4142135623730951


point1 = Point(3, 2)
point2 = Point(1, 4)

print(point1.distance_from_point(point2))     # 1.4142135623730951
