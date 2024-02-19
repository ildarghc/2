class House:

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


izbushka_on_chicken_legs = House()
izbushka_on_chicken_legs.setNewNumberOfFloors(1)
