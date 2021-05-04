print('Задача 5.')


# Пользователь вводит значение атрибута:
class Stationery:
    title = input('Введите название вашего инструмента: ручка, карандаш или маркер ')

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск письма')


class Pencil(Stationery):
    def draw(self):
        print('Запуск штриховки')


class Handle(Stationery):
    def draw(self):
        print('Запуск маркировки')


# Ветвление определяет, метод какого из подклассов запускать:
stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
if stationery.title == 'ручка':
    pen.draw()
elif stationery.title == 'карандаш':
    pencil.draw()
else:
    handle.draw()