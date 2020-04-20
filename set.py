# --------------- Тип данных МНОЖЕСТВО (set) ---------------
print()

    # Инициализация
print('------ ИНИЦИАЛИЗАЦИЯ ------')
temp_set = {}                                       # пустые скобки — тип dict
temp_set = {1, 2, 2, 3, 14, }                       # наполненные — тип set
temp_list = [121, 443, 32, 64, 55, 55, 51, 69]      # завели список с повторениями
temp_set = set(temp_list)                           # присвоили множеству значение списка
print(type(temp_set), temp_set)                     # нет повторений
print()

    # Обращения к элементам множества
print('------ ОБРАЩЕНИЯ К ЭЛЕМЕНТАМ МНОЖЕСТВА ------')
print(1 in temp_set)                                # Проверяем — есть ли цифра 1 в множестве temp_set. Ответ true/false

for element in temp_set:                            # В множествах нет понятия индекса (нумерации элементов), выводим только элементы
    print(element)
print()

    # Функции с множествами
print('------ ФУНКЦИИ С МНОЖЕСТВАМИ ------')
print('Длина множестава:', len(temp_set), 'элементов')
print()




print()

    # Методы
print('------ МЕТОДЫ ------')
print('Метод ADD — добавление элемента в множество.')
my_set_4.add(5)
print(my_set_4)
print()


print('Метод REMOVE — удаление элемента из множества.')
my_set_4.remove(1)            # Можно удалять только текстовые значения
print(my_set_4)
print()


print(1 in my_set_4)            # Возвращает true/false — есть ли в множестве число 1
print()

for el in my_set_4:
    print(el)
print()

    # Операции с множествами
print('------ ОПЕРАЦИИ С МНОЖЕСТВАМИ ------')
print('Пересечение — UNION')
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {5, 6, 7, 8, 9}

my_set_3 = my_set_1.union(my_set_2)             # .union — объединяет множества, убирая повторения
print(my_set_3)
print()

print('Разность — DIFFERENCE')
my_set_4 = my_set_1.difference(my_set_2)        # .difference — выкидывает элемент пересечения и всё, что указано в () после difference
print(my_set_4)


print('Задачка: Семейная пара собирается в отпуск, каждый собирает вещи')
# Max взял эти вещи:
max_things = {
    'телефон',
    'бритва',
    'рубашка',
    'шорты'
}
# Кейт взяла эти вещи:
kate_things = {
    'телефон',
    'шорты',
    'зонтик',
    'помада'
}
print('1. Какие вещи взяли супруги?')
print('ОБЪЕДИНЕНИЕ — обозначется вертикальным слешем "|"')
print(max_things | kate_things)
print()

print('2. Какие вещи повторяются?')
print('ПЕРЕСЕЧЕНИЕ — обозначается через "&"')
print(max_things & kate_things)
print()

print('3. Какие вещи не взял макс, но взяла кейт?')
print('РАЗНОСТЬ — обозначается через "-"')
print(kate_things - max_things)
print()

print('4. Какие вещи не взяла кейт, но взял макс?')
print(max_things - kate_things)
