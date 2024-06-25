class Building:

    total = 0

    def __init__(self, name):
        Building.total += 1
        self.name = name
        print(self.name)



for i in range(0,41):
    object = Building(f"Build{i}")
