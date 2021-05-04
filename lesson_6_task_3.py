print('Задача 3.')

# Предлагаем пользователю ввести оклад и премию сотрудника:
wage = int(input('Введите оклад сотрудника: '))
bonus = int(input('Введите премию сотрудника: '))
salary = {"wage": wage, "bonus": bonus}


# Пользователь вводит фамилию, имя, отчество и должность сотрудника:
class Worker:
    name = input('Введите имя сотрудника: ')
    surname = input('Введите фамилию сотрудника: ')
    position = input('Введите должность сотрудника: ')
    _income = salary

# Функция определяет полное имя сотрудника, складывая фамилию и имя через пробел:
    def get_full_name(self, name, surname):
        self.name = name
        self.surname = surname
        full_name = surname + ' ' + name
        return full_name

# Функция определяет полный доход сотрудника, суммируя значения ключей словаря с окладом и премией:
    def get_total_income(self, _income):
        self._income = _income
        return sum(salary.values())


worker = Worker()
print(f'{worker.get_full_name(worker.name, worker.surname)} получает {worker.get_total_income(worker._income)} на должности {worker.position}')