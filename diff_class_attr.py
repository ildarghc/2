class Building:
    total = 0

    def __init__(self):
        Building.total += 1


for i in range(40):
    some_building = Building()
    print('Объект класса Building №', Building.total, some_building)
