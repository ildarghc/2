class Car:
    price = 1000000

    def horse_powers(self):
        return 'количество лошидиных сил для автомобиля'


class Nissan(Car):
    price = 'nissan price'

    def horse_powers(self):
        return 'nissan hp'


class Kia(Car):
    price = 'kia price'

    def horse_powers(self):
        return 'kia hp'


# gt_r = Nissan()
# print(gt_r.price)
# print(gt_r.horse_powers())
#
# stinger = Kia()
# print(stinger.price)
# print(stinger.horse_powers())
