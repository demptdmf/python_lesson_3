# # --------------- Тип данных СТРОКА  (str) ---------------
#
#     # Инициализация
print('------ ИНИЦИАЛИЗАЦИЯ ЧЕРЕЗ КАВЫЧКИ ------ ')

temp_str = 'Mark Auto Volvo'
print(temp_str)
print()


    # Обращение к символам
print('------ ОБРАЩЕНИЕ К СТРОКАМ ------ ')
print('Вывод строки посимвольно (символ на каждой строчки)')
for i in range(len(temp_str)):
    print(temp_str[i])
print()

print('Срезы')
print(temp_str[1:4])    # 1 — начать со второго элемента, 0 — с начала, 4 — до 3 включительно.
print(temp_str[1:-3])   # -3 — это отрезать 3 символа с конца


    # Функции со строками
print('------ ФУНКЦИИ СО СТРОКАМИ ------ ')

print(temp_str, len(temp_str))      # len — выводит количество символов в строке
print(type(len))
print()


    # Операции со строками
print('------ ОПЕРАЦИИ СО СТРОКАМИ ------ ')
temp_str_2 = 'Mercedes'
print(temp_str + temp_str_2)    # Сложить строки, сложить данные, но лучше использовать форматирование.
print(temp_str_2 * 2)           # Помножить строки
print()


    # Форматирование строк
print('------ ФОРМАТИРОВАНИЕ СТРОК ------ ')

brand = 'Volvo'
price = 1.5
car = f'Марка: {brand} Цена: {price}'
print(car)
print(car.format(brand, price))     # старый вариант
print()


    # Методы
print('------ МЕТОДЫ ------ ')
print('Метод FIND — поиск подстроки в строке')

print(temp_str.find('Vol'))
print()

# SPLIT — разделение одной большой строки на подстроки

print('Метод SPLIT — разделение одной большой строки на подстроки')
print(temp_str.split())

cars = 'volvo,Audi,Lada'        # Если не будет пробелов — будет считаться одной строчкой
print(cars.split())             # Вывод будет: ['volvo,audi,lada']
print(cars.split(','))          # Вывод будет: ['volvo', 'audi', 'lada']
print()

print('Метод ISDIGIT — состоит ли строка только из цифр')
print(temp_str.isdigit())
number = '111'
print(number.isdigit())
print()

# Методы форматирования строк
print('Методы форматирования строк')
print(cars.upper())     # Верхний регистр VOLVO,AUDI,LADA
print(cars.title())     # Первая буквая большая Volvo,Audi,Lada
print(cars.lower())     # Нижний регистр volvo,audi,lada
print()

# Замена подстроки в строке
print('Замена подстроки в строке')
email_adress = 'Mail: _mail_'
email = 'my@gmail.com'
print(email_adress.replace('_mail_', email))     # _mail_ заменяем на значение переменной EMAIL благодаря .replace
print()