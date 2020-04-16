
friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ['admin', 'guest', 'user']


# Цикл FOR позволяет перебирать элементы последовательности по очереди, без цикла WHILE
# данный цикл очень полезен при выборке элементов из последовательности.

        # Как можно сделать через while (5 строк)
# i = 0
# while i < len(friends):
#     friend = friends[i]
#     print(friend)
#     i += 1


        # Как можно сделать через FOR (2 строки)

for friend in friends:
    print(friend)

print()

for letter in friend_name:
    print(letter)

print()

for role in roles:
    print(role)