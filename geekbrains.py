# Домашка гик
print('===== СТРОКИ =====')
print('вывести первых 3 победителей')
top5 = 'Первые 5 мест на соревнованиях: 1. Петров 2. Иванов 3. Сидоров 4. Орлов 5. Соколов'
start = top5.find('1')  # задаем переменной старт значение = ищем подстроку с цифрой 1
end = top5.find('4')    # переменной "конец" — ищем подстроку с цифрой 4
top3 = top5[start:end]  # Определяем топ3 — от цифры 1 до цифры 4.

result = f'Поздравляем: {top3} с успехом'
print(result)
print()

# ОПЕРАТОР IN
print('=== Оператор IN ===')
hero = 'Superman'
if 'man' in hero:  # Есть ли "man" в строке hero
    print('yes')

if hero.find('s') != -1:        # Функция find возвращает либо найденное условие, а если не нашло — присылает -1.
    print('YES')
else: print('no :(')

goals = ['Создать робота', 'вылечить ножку', 'здоровье']
if 'здоровье' in goals:
    print('Ok!')


# КОРТЕЖИ
print('=== КОРТЕЖИ ===')
print('Соревнования по Python')
count = int(input('Введите количество участников: '))
i = count                                   # Счетчик цикла — присваиваем count
members = []                                # участники
while i > 0:                                # пока счетчик > 0
    name = input(f'Кто занял {i} место? ')  # кто занял "такое-то" место
    members.append(name)                    # присваиваем в список "members" имя участника
    i -= 1                                  # каждые раз спрашивая следующее место (начиная с конца, 5е\4е\3е и т.д.)
print('В соревновании участвовали: ', members)

# Мы записывали людей с конца?
members.reverse()
print('В соревновании участвовали: ', members)

# Сделайте вывод первых трёх мест
result = members[:3]

print(f'Поздравляем победителей {result}')