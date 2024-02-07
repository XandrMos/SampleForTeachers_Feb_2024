class Vector:
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y
 
    def __str__(self) -> str:
        return "({0},{1})".format(self.x, self.y)
 
    def __add__(self, other) -> object:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
 
 
p1 = Vector(3, 6)
p2 = Vector(2, 3)
 
print(p1 + p2)