
print('1. вывести на экран 5 строк из нулей, каждую строку пронумеровать')

for i in range(5):
    print(i, '00000000000')
print()

print('2. В цикле юзер вводит 10 цифр. Найти количество введенных цифр 5')
count = 0
for n in range(10):
    n = int(input('Введите число: '))
    while n > 0:
        if n % 10 == 5:
            count += 1
        n = n // 10
print('Количество введенных цифр 5 — ', count)


print()
print('3. Найти сумму ряда чисел от 1 до 100:')
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

print()
print('4. Найти произведение ряда чисел от 1 до 10')
mult = 1
for i in range(1,11):
    mult *= i
print(mult)

print()
print('5. Вывести цифра числа на каждой строчке')
n = 249
i = 0
while n > 0:
    print(n % 10)
    n = n // 10

print()
print('РЕШЕНИЕ PRO — ПОСЛЕДОВАТЕЛЬНЫЙ ВЫВОД')
n = 249

count = 0                           # Делаем переменную для счетчика
el = 0                              # Делаем переменную для индекса
list = []                           # Создаем пустой список

while n > 0:
    list.insert(0, n % 10)          # Вставляем в начало списка значение n%10. Следующая вставка сдвинет элемент на след индекс.
    count += 1                      # Добавляем счетчику значение +1
    n = n // 10                     # Переходим к след цифре в числе (с конца)

for el in range(count):             # Для элемента в диапазоне "счетчика"
    print(list[el])                 # печатать элемент списка


print()
print('6. Найти сумму цифр числа')
n = 249
sum = 0
while n > 0:
    integer = n % 10
    sum += integer
    n = n // 10
print(sum)

while n > 0:
    sum = sum + (n % 10)        # в переменную sum добавляем крайнюю правую цифру числа N
    n = n // 10                 # затем эту цифру отсекаем (ее мы уже отработали), далее цикл заново идет и уже работает с 2, добавляет ее к sum по такому же принципу
print(sum)

print()
print('7. Найти произведение цифр числа')
n = 249
mult = 1
while n > 0:
    mult = mult * (n % 10)
    n = n // 10
print(mult)


print()
print('8. Есть ли среди цифр число 5?')
n = 249
while n > 0:
    if n % 10 == 5:
        print('Есть')
        break
    n = n // 10
else:
    print('no.')


print()
print('9. Найти максимальную цифру в числе')
n = 249
max = 0
while n > 0:
    if n % 10 > max:
        max = n % 10
    n = n // 10
print(max)
print()

print('10. Найти количество цифр 5 в числе')
count = 0
n = 2455
while n > 0:
    if n % 10 == 5:
        count += 1
    n = n // 10
print(count)
