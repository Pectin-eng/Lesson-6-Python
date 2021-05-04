print('Задача 5.')

# Записываем числа в файл программно:
f = open('task_5.txt', 'w')
string = "6 3 1 9 4 2"
f.write(string)

# При помощи цикла разделяем строку на отдельные символы и собираем все численные значения в список lin:
lin = []
with open('task_5.txt', 'r') as file:
    for i in string:
        string.split()
        if i == ' ':
            pass
        else:
            lin.append(i)

# Переводим значения из строкового формата в численный и вычисляем их сумму:
print('Сумма чисел в файле:', sum(map(int, lin)))

f.write(string)
f.close()