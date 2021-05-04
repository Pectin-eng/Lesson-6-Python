from time import sleep
print('Задача 1.')


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

# Метод отображает сообщение и выдерживает заданное количество времени.
# Ограничение на количество сообщений задано во избежание бесконечного цикла:
    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор 'f' {TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()

