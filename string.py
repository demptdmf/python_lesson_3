# # --------------- Тип данных СТРОКА  (str) ---------------
#
#     # Инициализация
temp_str = 'Mark Auto Volvo'
# print(temp_str)
# # temp_str = ""
#
#
#
#     # Обращение к символам

# Вывод строки посимвольно (символ на каждой строчки)
# for i in range(len(temp_str)):
#     print(temp_str[i])

# Срезы
# print(temp_str[1:4])    # 1 — начать со второго символа, 0 — с начала, 4 — до 3 включительно.
# print(temp_str[1:-3])   # -3 — это отрезать 3 символа с конца

    # Функции со строками
print(temp_str, len(temp_str))      # len — выводит количество символов в строке
print(type(len))

    # Операции со строками
temp_str_2 = 'Mercedes'
print(temp_str + temp_str_2)    # Сложить строки, сложить данные, но лучше использовать форматирование.
print(temp_str_2 * 2)           # Помножить строки


    # Форматирование строк
brand = 'Volvo'
price = 1.5
car = f'Марка: {brand} Цена: {price}'
print(car)


    # Методы
# SPLIT — разделение одной большой строки на подстроки
print(temp_str.split())

cars = 'volvo,Audi,Lada'        # Если не будет пробелов — будет считаться одной строчкой
print(cars.split())             # Вывод будет: ['volvo,audi,lada']
print(cars.split(','))          # Вывод будет: ['volvo', 'audi', 'lada']

# Методы форматирования строк
print(cars.upper())     # Верхний регистр VOLVO,AUDI,LADA
print(cars.title())     # Первая буквая большая Volvo,Audi,Lada
print(cars.lower())     # Нижний регистр volvo,audi,lada

# Замена подстроки в строке
email_adress = 'Mail: _mail_'
email = 'my@gmail.com'
print(email_adress.replace('_mail_',email))     # _mail_ заменяем на значение переменной EMAIL благодаря .replace