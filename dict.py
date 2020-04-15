# --------------- Тип данных СЛОВАРИ (dict) ---------------
# Инициализация
print('------ ИНИЦИАЛИЗАЦИЯ ------ ')
print('Обычная, через фигурные скобки {}')
dict_temp = {}                      # Пустой словарь
print(type(dict_temp), dict_temp)   # Вывод типа словаря (тип dict) и вывод самого словаря

# Занесение различных данных в словарь

dict_temp = {
    'dict1': 1,
    'dict2': 2.1,
    'dict3': 'name',
    'dict4': [1, 2, 3, 4]
}

print(type(dict_temp), dict_temp)
print()

print('С помощью FROMKEYS')
dict_temp = dict.fromkeys(['a', 'b'], [12, '2020'])               # будет создан словарь, у когорого элементы будут A и B, значения которых — вписаны рядом. Не забыть про квадратные скобки.
print(type(dict_temp), dict_temp)
print()

print('С помощью DICT')
dict_temp = dict(brand = 'Volvo', volume_engine = 1.5)          # Словарь
print(type(dict_temp), dict_temp)
print()

print('С помощью генератора')
dict_temp = {a: a ** 2 for a in range(10)}              # От 0 до 10 печатаем значения а, возведенные в квадрат
print(type(dict_temp), dict_temp)
print()



    # Обращение к содержимому словаря
print('------ ОБРАЩЕНИЕ К СОДЕРЖИМОМУ СЛОВАРЯ ------ ')
print('Вывод конкретного ключа из словаря')
dict_temp = {a: a ** 2 for a in range(10)}
print(dict_temp[8])                       # Просим вывести 8 ключ словаря (8: 64) — будет выведено число 64
print()

    # Функции со словарями
print('------ ФУНКЦИИ СО СЛОВАРЯМИ ------ ')
print('Функция KEYS — получить все ключи словаря')
print(dict_temp.keys())                 # Возращается специальный тип dict_keys, но с таким не работают, нужно привести к листу:
print(list(dict_temp.keys()))
print()

print('Функция VALUES — получить все значения словаря')
print(list(dict_temp.values()))         # Получить все значения — то, результаты возведения в квадрат
print()

print('Функция ITEMS — получить пары ключ-значений')
print(list(dict_temp.items()))          # Возвращает кортежи. Кортежи — это лист, но неизменяемый.
print()


    # Работа с элементами
print('------ РАБОТА С ЭЛЕМЕНТАМИ ------ ')
print('Присвоить к конкретному ключу определенное значение')
dict_temp[0] = 100
print(type(dict_temp), dict_temp)
print()

print('Добавление пар-ключей значениям')
dict_temp['name'] = 'me'                # Добавляем в словарь ключ NAME с любым значением (например, ME)
print(type(dict_temp), dict_temp)
print()


    # Методы
print('------ МЕТОДЫ ------ ')
# keys, values, item см выше
print('Метод POP — удаляет значение по ключу. Необходимо для редактирование словарей.')

temp = dict_temp.pop('name')                   # Удаляет вышеуказанное значение name из словаря
print(temp, '— это значение будет удалено из словаря (строка 59)')
print(type(dict_temp), dict_temp)
print()


    # Итерирование по словарю
print('------ ИТЕРИРОВАНИЕ ПО СЛОВАРЮ ------ ')     # Итерирование — пройтись по словарю
print('Через парные значения')
for pair in dict_temp.items():                      # вывести парные значения словаря
    print(pair)
print()

# !!! pair — Это пара, но удобно работать с конкретными элементами словаря !!!


print('По конкретным элементам, без применения списка')
for key, value in dict_temp.items():                 # key — это первый элемент в паре (ключ), value — второй элемент (значение)
    print(key, value)
print()

print('По ключам. Выводим только ключи словаря')
for key in dict_temp.keys():
    print(key)
print()

print('По ключам. Сокращенный код')
for key in dict_temp:
    print(key)
print()

print('По значениям. Выводим только значения ключей.')
for value in dict_temp.values():
    print(value)
print()

print()