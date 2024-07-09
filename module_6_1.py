class Animal:

    def __init__(self, name):
        self.name = name
        self.alive = name.alive
        self.fed = name.fed
class Plant:

    def __init__(self, name):
        self.name = name
        self.edible = name.edible

class Mammal(Animal):

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.alive = True
    def eat(self, food):
        if food.edible is True:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}.")
class Predator(Animal):

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.alive = True
    def eat(self, food):
        if food.edible is True:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}.")

class Flower(Plant):

    def __init__(self, name):
        self.name = name
        self.edible = False

class Fruit(Plant):
    
    def __init__(self, name):
        self.name = name
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)