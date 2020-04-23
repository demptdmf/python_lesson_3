# --------------- Тип данных КОРТЕЖ (tuple) ---------------

print()
    # Инициализация
print('------ ИНИЦИАЛИЗАЦИЯ ------')
print('------ Обычная, через круглые скобки () ------ ')
temp_tuple = (1, 2, 3)                                  # Создание пустого кортежа
print(type(temp_tuple), temp_tuple)                     # Напечатать тип кортежа — получится тип кортеже "кортеж"
print()

print('------ Из листа (list) ------ ')
temp_list = [1, 2, 3]
temp_tuple = tuple(temp_list)               # Преобразование типов. Перевести лист в кортеж с цель экономии места.
print(type(temp_tuple), temp_tuple)
print()

    # Обращения к элементам кортежа
print('------ ОБРАЩЕНИЯ К ЭЛЕМЕНТАМ КОРТЕЖА ------')
for i in range(len(temp_tuple)):
    print(temp_tuple[i])


    # Функции с кортежами
print('------ ФУНКЦИИ С КОРТЕЖАМИ ------')

print('Длина кортежа:', len(temp_tuple), 'элемента')
print()


    # Операции с кортежами
print('------ ОПЕРАЦИИ С КОРТЕЖАМИ ------')
temp_tuple_2 = (3.3, 4.4, 'volvo')                     # У кортежа не может быть единственное значение STR, только внутри него
print('Сложение кортежей:', temp_tuple + temp_tuple_2)
print('Множить кортежи, превращая их в один:', temp_tuple * 2)
print()


    # Методы
print('------ МЕТОДЫ ------')
print('!! Могут быть только те, которые не изменяют кортежи, т.к. в этом их главное отличие — неизменяемость !!')


# # SORT
print('Метод Sort — сортировка (от наименьшего к наибольшему)')
temp_tuple = [9, 3, 5, 8, 6, 2]
temp_tuple.sort()
print(temp_tuple)
print()



    # Обработка кортежей (map, filter, reduce)
print('------ ОБРАБОТКА КОРТЕЖЕЙ ------')

# MAP
print('Map — функция, применяемая к каждому элементу кортежа')
temp_tuple = [9, 3, 5, 8, 6, 2]

#конструкция: map(function, tuple) возвращает тип —---> map приводим к типу tuple от map ---> tuple(map)

# new_temp_tuple = tuple(map(str, temp_tuple))
new_temp_tuple = tuple(map(lambda x: x ** 2, temp_tuple))
print(new_temp_tuple, '— теперь каждый элемент возведен в квадрат')
print()

# FILTER
print('Filter — фильтрация кортежа согласно условиям')
temp_tuple = [9, 3, 5, 8, 6, 2]
new_temp_tuple = tuple(filter(lambda x: x < 5, temp_tuple))
print(new_temp_tuple, '— выведены все цирфы кортежа, меньше 5')
print()

# REDUCE
print('Reduce — применяется ко всем элементам кортежа и возвращает некоторый один элемент')
new_temp_tuple = [1, 2, 3, 4]
from functools import reduce
sum = reduce(lambda x,y: x+y, temp_tuple)
product = reduce(lambda x,y: x*y, temp_tuple)
print(sum, '— сумма элементов листа;', product, '— произведение элементов листа')
print()

    # Хранение
print('------ ХРАНЕНИЕ КОРТЕЖЕЙ ------')

temp_list = [1, 2, 3]               # создаем список для сравнения
temp_tuple = (1, 2, 3)              # и кортеж
print('Размер списка:', temp_list.__sizeof__())                 # проверка размера списка
print('Размер кортежа WOW SUPER:', temp_tuple.__sizeof__())     # проверка размера кортежа