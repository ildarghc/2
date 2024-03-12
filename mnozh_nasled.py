# https://urban-university.ru/members/courses/course999421818026/20231106-0000domasnee-zadanie-po-teme-mnozestvennoe-nasledovanie-290139472637
# ПРАКТИЧЕСКОЕ ЗАДАНИЕ
# 2023/11/06 00:00|Домашнее задание по теме "Множественное наследование"
# # Создайте новый проект или продолжите работу в текущем проекте
# # Ваша задача:
# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
# которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
# а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price
# Получившийся код прикрепите к заданию текстом

class Vehicle:
    vehicle_type = 'none'


class Car:
    price = 1000000

    def horse_powers(self):
        return 'количество лошадиных сил для автомобиля'


class Nissan(Car, Vehicle):
    vehicle_type = 'nissan_type'
    price = 'nissan_price'

    def horse_powers(self):
        return 'nissan_hp'


junior = Nissan()
print(junior.vehicle_type, junior.price, sep=', ')
