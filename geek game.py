number = 42
# Шаг 1. Загадываем число.
import random                           # Импортируем рандом
number = random.randint(1, 100)         # присваиваем рандом для переменной в виде числа рандом от 1 до 100
user_number = None
count = 0                   # Количество попыток. Создаем переменную count
levels = {1: 10, 2: 5, 3: 3}
level = int(input('Выберите уровень сложности от 1 до 3, где 3 - хардкор: '))
max_count = levels[level]               # Количество максимальных попыток зависит от уровня сложности

while number != user_number:
    count += 1
    if count > max_count:
        print('GAME OVER')
        break
    print(f'Попытка №{count}')
    # Шаг 2. Предлагаем пользователю ввести число
    user_number = int(input('Введи число от 1 до 100: '))
    # Шаг 3. Сравнение числа, вывод результата
    if number < user_number:
        print('Число больше загаданного.')
    elif number > user_number:
        print('Число меньше загаданного.')
else:
    print('DIGITAL-DETKA !!! ПИУ ПИУ ПИУ!')