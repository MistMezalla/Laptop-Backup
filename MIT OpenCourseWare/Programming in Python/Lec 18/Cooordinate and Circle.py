class Coordinate(object):
    def __init__(self, abs, ord):
        self.x = abs
        self.y = ord

    def dist_origin(self):
        return (self.x**2+self.y**2)**0.5

    def dist_bet_pts(self,other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'


pt1 = Coordinate(3,4)
pt2 = Coordinate(-7,6)
print("Cooordinates of p1: ",pt1.x,',', pt1.y)
print(pt1)
print(pt2)
print(pt1.dist_origin())
print(pt2.dist_origin())
print(pt1.dist_bet_pts(pt2))

class Circle(object):
    def __init__(self, center, rad):
        self.r = rad
        self.center = center

    def is_inside(self,pt):
        if (self.center.dist_bet_pts(pt) <= self.r):
            return True
        else:
            return False
    def __str__(self):
        return 'Radius = ' + str(self.r)+'\tand\tCenter = ' + str(self.center)


Circle_1 = Circle(pt1, 5)
print(Circle_1)

pt3 = Coordinate(0,0)
Circle_2 = Circle(pt3,5)
print(Circle_2)
pt4 = Coordinate(10,-10)
print(pt4)
print(Circle_2.is_inside(pt4))
print(Circle_2.is_inside(pt1))
