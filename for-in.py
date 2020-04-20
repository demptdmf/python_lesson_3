
friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ['admin', 'guest', 'user']


# Цикл FOR позволяет перебирать элементы последовательности по очереди, без цикла WHILE
# данный цикл очень полезен при выборке элементов из последовательности.

        # Как можно сделать через while (5 строк)
i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1


        # Как можно сделать через FOR (2 строки)

for friend in friends:
    print(friend)

print()

for letter in friend_name:
    print(letter)

print()

for role in roles:
    print(role)


words = ['cat', 'window', 'defenestrate']
for w in words[:]:              # Цикл по срезу-копии целого списка. Для букв в "словах"
    if len(w) > 6:              # Если длина слова > 6 (если количество букв > 6)
        words.insert(0, w)      # Вставляем в начало списка то слово, длина которого > 6 букв
        print(words)            # Выводим обновленный список
