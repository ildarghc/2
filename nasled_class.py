class Car:
    price = 1000000

    def __init__(self):
        self.hp = 100

    def horse_powers(self):
        self.hp = 'new car hp'


class Nissan(Car):
    price = 'nissan price'

    def horse_powers(self):
        self.hp = 'nissan hp'


class Kia(Car):
    price = 'kia price'

    def horse_powers(self):
        self.hp = 'kia hp'


gt_r = Nissan()
print(gt_r.price)
gt_r.horse_powers()
print(gt_r.hp)

stinger = Kia()
print(stinger.price)
stinger.horse_powers()
print(stinger.hp)
