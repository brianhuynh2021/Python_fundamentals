class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y

point1 = Point(10, 10)
print(Point(10, 10).getX())
print(point1.x)
