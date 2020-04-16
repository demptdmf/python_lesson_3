# Когда использовать RANGE
# позволяет создать последовательность целых чисел
numbers = range(10)
print(numbers)
print(type(numbers), '— это диапазон')

print(list(range(1, 100, 2)))               # Напечатать список от 1 до 100 с шагом "2" — 1+2, 3+2, 5+2 и так далее

for number in range(1, 100, 2):             # Просто напечатать эти же самые цифры, но без списка
    print(number)

print()

winners = ['Max', 'Leo', 'Kate']
for i in range(1, len(winners)):       # Для элемента в диапазоне длины списка winners
    print(i+1, winners[i])          # выводить номер элемента (+1, иначе начало будет с 0, т.к. это список) и его значение


