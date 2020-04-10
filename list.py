# # --------------- Тип данных СПИСОК (list) ---------------

print()
    # Инициализация
print('------ ИНИЦИАЛИЗАЦИЯ ------')
print('------ Обычная, через квадратные скобки [] ------ ')
list_temp = []                              # Создание пустого списка
print(type(list_temp))                      # Напечатать тип списка — получится тип списка "список"
print()

list_temp = [1.2, 123, 'Volvo', [1,2,3]]
for el in list_temp:                        # el - обозначение каждого элемента в list_temp, перечисленные через запятую
    print(el, type(el))                     # выводим этот каждый элемент и рядом пишем его тип
print()

# С помощью команды list
print('С помощью команды list:')
list_str = list('volvo')                    # строка вольво — представилась в виде отдельных букв и каждая буква представляет собой элемент списка
print(list_str)                             # получается ['v', 'o', 'l', 'v', 'o']
print()


    # Обращения к элементам списка, подсписки
print('------ ОБРАЩЕНИЯ К ЭЛЕМЕНТАМ СПИСКА, ПОДСПИСКАМ ------')
for i in range(len(list_temp)):
    print(i, ':', list_temp[i])
print()

print('Срезы c начала списка до конца — каждую строчку отсекается первый элемент:')
for i in range(len(list_temp)):
    print(i, ':', list_temp[i:])            # i: — означает, что срез будет с первого и до последнего элемента
print()

print('Срезы в обратном порядке:')
for i in range(len(list_temp)):
    print(i, ':', list_temp[:i])            # :i — означает, что срез будет с первого и до последнего элемента
print()


    # Функции со списками
print('------ ФУНКЦИИ СО СПИСКАМИ ------')

print('Длина списка:', len(list_temp))
print()


    # Операции со списками
print('------ ОПЕРАЦИИ СО СПИСКАМИ ------')

print('Сложение списков:', list_temp + list_str)
print('Множить списки, превращая их в один:', list_temp * 2)
print()


    # Методы
print('------ МЕТОДЫ ------')
# APPEND
print('Метод Append — для добавления в конец списка')
integer_list = []
print(integer_list, '— сейчас лист пустой, без цифр и символов')
for i in range(5):                          # Наполняем список целыми числами
    integer_list.append(i)                  # Каждый раз в цикле будет присоединяться новое число от 0 до 4
print(integer_list, '- теперь метод добавляет в список наши цифры из цикла')
integer_list.append(0)
print(integer_list, '— а здесь метод добавляет в конец списка число, указанное в методе append')
print()

# REMOVE
print('Метод Remove — удаление первого указанного и встретившегося элемента из списка')
integer_list.remove(0)                      # просим удалить 0
print(integer_list, '— удалили первый найденный указанный элемента')
print()

# DEL
print('Метод Del — удаление конкретного элемента списка')
del integer_list[2]                         # удаляем указанный элемент (0 - это первый элемент (цифра 1), 1 — это второй элемент (цифра 2), и тд.). У нас второй элемент — цифра 3.
print(integer_list,'- второй элемент списка (цифра 3) — удалена') # элемент 2 (цифра 3) — удалена
print()

# INSERT
print('Метод Insert — вставка элемента !вместо! определенной позиции')
integer_list.insert(2, 100)
print(integer_list, '— вставили "100" после второй позиции')
print()

# REVERSE
print('Метод Reverse — обратный порядок элементов списка')
integer_list.reverse()
print(integer_list)
print()

# SORT
print('Метод Sort — сортировка (от наименьшего к наибольшему)')
integer_list = [9, 3, 5, 8, 6, 2]
integer_list.sort()
print(integer_list)
print()


    # Обработка списков (map, filter, reduce)
print('------ ОБРАБОТКА СПИСКОВ ------')
# MAP
print('Map — функция, применяемая к каждому элементу списка')
integer_list = [9, 3, 5, 8, 6, 2]

#конструкция: map(function, list) возвращает тип —---> map приводим к типу list от map ---> list(map)

# new_integer_list = list(map(str, integer_list))
new_integer_list = list(map(lambda x: x ** 2, integer_list))
print(new_integer_list, '— теперь каждый элемент возведен в квадрат')
print()

# FILTER
print('Filter — фильтрация списка согласно условиям')
integer_list = [9, 3, 5, 8, 6, 2]
new_integer_list = list(filter(lambda x: x < 5, integer_list))
print(new_integer_list, '— выведены все цирфы списка, меньше 5')

# REDUCE
print('Reduce — применяется ко всем элементам списка и возвращает некоторый один элемент')
integer_list = [1, 2, 3, 4]
from functools import reduce
sum = reduce(lambda x,y: x+y, integer_list)
product = reduce(lambda x,y: x*y, integer_list)
print(sum, '— сумма элементов листа;', product, '— произведение элементов листа')