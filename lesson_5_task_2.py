print('Задача 2.')

file = open('task_2.txt', 'w')
# Программно вводим в файл несколько строк:
file.write('Hello, world!\nI am a GeekBrains student.\nI learn Python.')
file.close()

f = open('task_2.txt', 'r')

# Цикл вычисляет количество строк в файле и количество слов, разделенных пробелом в каждой строке:
i = 0
with open(r"task_2.txt", "r") as file:
    for line in file:
        i = i + 1
        line = line.split()
        l = len(line)
        if l < 5:
            pass
        else:
            print(f'В строке {i}: {l} слов')
        if l < 5:
            print(f'В строке {i}: {l} слова')
f.close()