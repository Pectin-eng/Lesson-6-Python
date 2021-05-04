print('Задача 3.')

f = open('task_3.txt', 'w')

state = []
# Вводим цикл для заполнения пользователем:
i = 1
# К каждой введенной строке добавляем знак переноса:
while True:
    string = input('Введите фамилию сотрудника и его оклад через пробел: ')
    enter = '\n'
    d = string + enter
    state.append(d)
    f.writelines(state)
    if input('Информация добавлена. Продолжить ввод? да/нет ') == 'нет':
        break
    i += 1

f.close()

with open('task_3.txt', 'r') as file:
    salary = []
    surname = []
    string = f.read().strip().split('\n')
# При помощи цикла преобразуем строки в список, разделяя элементы по пробелу, находим,
# в какой строке значение второго элемента не превышает 20 000, добавляем первый элемент этого списка в список
# surname, а вторые элементы остальных собираем в список salary:
    for i in string:
        i = i.split()
        if int(i[1]) < 20000:
            surname.append(i[0])
        else:
            pass
        salary.append(i[1])

print(f'Оклад меньше 20.000 имеет {p}, средняя зарплата', "{:.2f}".format(sum(map(int, salary)) / len(salary)))
