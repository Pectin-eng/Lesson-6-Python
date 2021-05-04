print('Задача 4.')

my_list = []
# Цикл заменяет в файле каждое выбранное значение строки на другое введенное значение и записывает
# результат в список my_list:
with open(r"task_4.txt", "r") as file:
    for line in file:
        line = line.replace('One', 'Один')
        line = line.replace('Two', 'Два')
        line = line.replace('Three', 'Три')
        line = line.replace('Four', 'Четыре')
        my_list.append(line)

# Результат из списка my_list записывается в новый файл:
with open("task_4.1.txt", "w") as file:
    file.writelines(my_list)

file.close()
