class Entity:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def __str__(self):
         return f"{self.id}: x: {self.x}, y: {self.y}"


class Mob(Entity):
    def __init__(self, id, x, y, speed):
        super().__init__(id, x, y)
        self.speed = speed

    def move(self, dir):
        if dir == "n":
            self.y -= self.speed
        elif dir == "s":
            self.y += self.speed
        elif dir == "w":
            self.x -= self.speed
        elif dir == "e":
            self.x += self.speed

    def __str__(self):
        return super().__str__() + f", spd: {self.speed}"


e = Entity(0, 10, 10)

m = Mob(1, 10, 20, 2)



print(e)
print(m)