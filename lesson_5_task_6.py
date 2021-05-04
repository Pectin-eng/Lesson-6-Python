print('Задача 6.')

amount = []
disc = []
numbers = []
# При помощи цикла разделяем строки по пробелам и извлекаем сначала все численные значения, а затем названия
# предметов в начале строк, отрезая двоеточия при помощи метода срезов:
# disc = список с названиями предметов;
# numbers = список с количеством всех часов по предметам;
# amount = список с суммами часов по каждому предмету.
with open('task_6.txt') as file:
    for line in file:
        string = line.split()
        numbers.append([el for el in string if el.isnumeric()])
        disc.append(string[0][:-1])

# Суммируем числовые значения для каждой строки:
for i in numbers:
    amount.append(sum(map(int, i)))
# Передаем данные в словарь:
print('Общее количество часов по предметам:')
print(dict(zip(disc, amount)))
