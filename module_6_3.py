class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = "Frrr"
        super().__init__()


    def run(self, dx):
        self.x_distance += dx
        super().__init__()

class Eagle:

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        super().__init__()

    def fly(self, dy):
        self.y_distance += dy
        super().__init__()


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)

print(Pegasus.mro())
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
