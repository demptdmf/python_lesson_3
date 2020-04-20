# Когда использовать RANGE
# позволяет создать последовательность целых чисел
numbers = range(10)
print(numbers)
print(type(numbers), '— это диапазон')

print(list(range(1, 20, 2)))               # Напечатать список от 1 до 20 с шагом "2" — 1+2, 3+2, 5+2 и так далее

for number in range(1, 20, 2):             # Просто напечатать эти же самые цифры, но без списка
    print(number, '-', type(number))

print()

winners = ['Max', 'Leo', 'Kate']
for i in range(1, len(winners)):        # Для элемента в диапазоне длины списка winners
    print(i, winners[i])              # выводить номер элемента (+1, иначе начало будет с 0, т.к. это список) и его значение

print()

print('Вывод простых чисел')
for n in range(2, 10):                          # для числа от 2 до 9
     for x in range(2, n):                      # для множителя (х) от 2 до числа N
         if n % x == 0:                         # если остаток деления N на X = 0 (если число N делится на Х без остатка)
             print(n, 'равно:', x, '*', n//x)   # то печатать это число N с условием: оно берется из "множитель" * "число/множитель"
             break
     else:                                      # цикл потерпел неудачу, не найдя множитель
         print(n, '— это простое число')

print()

print('Вывод через CONTINUE \n'
      'Оператор continue продолжает выполнение со следующей итерации цикла')

for num in range(2, 10):
     if num % 2 == 0:
         print(num, '— четное число')
         continue                       # идет сразу к след строчке кода, и потом повторяется if.
     print(num, '— нечетное число')

print()

for num in range(2, 10):
    if num % 2 == 0:
        print(num, '— четное число')
    else:
        print(num, '— нечетное число')

# В первом случае мы идем подряд по коду, и условием является "после найденного четного числа к следующему числу пишем "нечетное".
# Во втором примере мы перебираем цифры, и если число делится на 2 — пишем "четное", если нет — "нечетное"
