import math

class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]

    def distance(self):
        x_part = self.x2 - self.x1
        y_part = self.y2 - self.y1
        return math.sqrt( (x_part ** 2) + (y_part ** 2) )


    def slope(self):
        top = self.y2 - self.y1
        bottom = self.x2 - self.x1
        return top / bottom

class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        left = 2 * math.pi * self.radius * self.height
        right = 2 * math.pi * (self.radius ** 2)
        return left + right

# Tests
# coordinate1 = (3,2)
# coordinate2 = (8,10)
#
# li = Line(coordinate1,coordinate2)
#
# li.distance() # 9.433981132056603
# li.slope() # 1.6

# c = Cylinder(2,3)
# c.volume() #56.52
# c.surface_area() #94.2
