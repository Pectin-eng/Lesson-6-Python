print('Задача 4.')


# Пользователь вводит атрибуты всего класса:
class Car:
    speed = int(input('Введите вашу скорость: '))
    color = input('Введите цвет машины: ')
    name = input('Введите марку машины: ')
    is_police = input('У вас полицейская машина? да/нет ')

    def go(self, color, name):
        print(f'{color} {name} поехала.')

    def show_speed(self, speed):
        print(f'Скорость {speed}')

    def turn(self, color, name, turn):
        turn = input('Куда будем поворачивать? ')
        print(f'{color} {name} повернула {turn}.')

    def stop(self, color, name):
        print(f'{color} {name} остановилась.')


class TownCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            print('Скорость превышена.')
        else:
            print(f'Скорость {speed}')


class SportCar(Car):
    def go(self, color, name):
        print(f'{color} {name} поехала.')


class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 40:
            print('Скорость превышена.')
        else:
            pass


class PoliceCar(Car):
    def police(self, is_police):
        if is_police == 'да':
            print('Вы полицейский.')
        else:
            print('Вы не полицейский.')


# В консоль по очереди выводятся экземпляры каждого подкласса:
car = Car()
town_car = TownCar()
town_car.go(car.color, car.name)
town_car.show_speed(car.speed)
town_car.turn(car.color, car.name, car.turn)
town_car.stop(car.color, car.name)

sport_car = SportCar()
sport_car.go(car.color, car.name)
sport_car.show_speed(car.speed)
sport_car.turn(car.color, car.name, car.turn)
sport_car.stop(car.color, car.name)

work_car = WorkCar()
work_car.go(car.color, car.name)
work_car.show_speed(car.speed)
work_car.turn(car.color, car.name, car.turn)
work_car.stop(car.color, car.name)

police_car = PoliceCar()
police_car.go(car.color, car.name)
police_car.show_speed(car.speed)
police_car.turn(car.color, car.name, car.turn)
police_car.stop(car.color, car.name)