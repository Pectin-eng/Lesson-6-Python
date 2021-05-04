print('Задача 7.')

import json

numbers = []
names = []
profit = []
# При помощи цикла разделяем каждую строку на элементы по пробелам, извлекаем численные элементы
# отдельно для каждой строки, а также отдельно извлекаем названия фирм:
# numbers = список численных значений для каждой строки;
# names = список названий фирм;
# profit = прибыль или убыток для каждой фирмы;
with open('task_7.txt', 'r') as file:
    for line in file:
        string = line.split()
        numbers.append([el for el in string if el.isnumeric()])
        names.append(string[0])

# Вычисляем разность между прибылью и издержками для каждой фирмы:
for i in numbers:
    profit.append(int(i[0]) - int(i[1]))

# Отсекаем все убыточные показатели:
profit_list = ([i for i in profit if i > 0])

# Вычисляем средний показатель прибыли:
average_profit = (["%.2f" % ((sum(profit_list)) / (len(profit_list) + 1))])

# Создаем словарь с названиями фирм и их прибылью или убытками:
firm_profit = (dict(zip(names, profit)))

# Создаем словарь со средним значением прибыли без учета убытков:
total = (dict(zip(['average_profit'], average_profit)))

# Создаем итоговый словарь со значениями прибыли либо убытков каждой фирмы и средним значением прибыли:
total_list = [firm_profit, total]

print('Прибыль и убытки каждой фирмы, а также среднее значение прибыли без учета убытков:')
print(total_list)

# Создаем файл json и записываем в него результат:
with open('json_task_7.json', 'w') as file:
    json.dump(total_list, file)

