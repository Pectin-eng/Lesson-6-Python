print('Задача 2.')


class Road:
    _length = int(input('Введите длину дороги: '))
    _width = int(input('Введите ширину дороги: '))

# Функция расчитывает необходимую массу асфальта согласно заданным пользователем параметрам по заданной формуле:
    def calc(self, _length, _width, weight, thick):
        self.length = _length
        self.width = _width
        self.weight = weight
        self.thick = thick
        calc = self.length * self.width * self.weight * self.thick
        return calc


road = Road()
print(f'Необходимо {road.calc(road._length, road._width, 25, 5)} кг.')