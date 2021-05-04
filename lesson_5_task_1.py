print('Задача 1.')

file = open('task_1.txt', 'w')

# Для последовательного ввода нескольких строк создаем цикл:
str_list = []
# В цикле к каждой введенной строке добавляем знак переноса строки:
while True:
    record = input('Сделайте запись в файл. Для окончания записи введите пробел: ')
    enter = '\n'
    string = record + enter
    str_list.append(string)
    file.writelines(str_list)
# Условие окончания записи - пробел:
    if string == ' ' + enter:
        break
file.close()
