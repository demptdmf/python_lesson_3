f = open('text.txt')
text = f.read()
print('1) Методами строк очистить текст от знаков препинания:')
text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace('?', '')
text = text.replace('!', '')
text = text.replace('«', '')
text = text.replace('»', '')
text = text.replace(':', '')
text = text.replace(';', '')
text = text.replace('—', '')

print(text)
print(type(text))
print()
# ---- ВОПРОС ----
# 1. Хотел сделать в единой строке через or/and/& — но все условия не выполнялись. Сделал вручную, можно как-то сразу всё?
''' ОТВЕТ:
symbols = [",", ".", ":", ";", "!", "?", "—", "»","«","(",")"]
for symbol in symbols:
    text = text.replace(symbol,"")
'''


print('2) Сформировать list со словами (split):')
text_list = text.split()
print(type(text_list))
print()


print('3) Привести все слова к нижнему регистру (map);')
new_list = list(map(lambda letters: letters.lower(), text_list))
print(new_list)
print(type(new_list))
print()



print('4) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;')
dict_text = {}
for word in new_list:
    dict_text[word] = new_list.count(word)
print(dict_text)

# for word in dict_text.items():
#     print(word)


# В ЦИКЛЕ БЕРЕТСЯ ПЕРВОЕ СЛОВО,
# ОБХОДИТСЯ ПО СПИСКУ,
# СЧИТАЕТ КОЛВО ПОВТОРЕНИЙ,
# ЗАПИСЫВАЕТСЯ В СЛОВАРЬ ПОД КЛЮЧЕМ С СООТВЕТСВУЮЩИМ ИМЕНЕМ,
# И ПЕРЕХОДИТ К СЛЕДУЩЕМУ ЭЛЕМЕНТУ


# Это сложная часть задания, но решаемая не сложно, просто в голове нужно определить порядок действий:
# 1. Вы уже должны были получисть какойто список слов из текста допустим list_
# 2. Теперь можно например задать какой то пустой словарь:
# dict_text = {}
# 3. Потом пройтись циклом по списку слов:
# for word in list_:
# 4. И для каждого слова в списке, добавлять в пустой словарь, к соответсвующему ключу значение, которое получить можно с помощью метода списков "count".
# Этот метод вызываем для какого то списка, и указываем слово, чье количество повторений нам интересно
# сперва цикл возьмет первое слово в списке, запишет его ключом в словарь, а потом присоединит к нему значение кол-ва повторений, и так по следущему и следующему слову до конца списка
# ->dict_text[word] = list_.count(word)
# допустим, взгляните на решение выше
# В ЦИКЛЕ БЕРЕТСЯ ПЕРВОЕ СЛОВО,
# ОБХОДИТСЯ ПО СПИСКУ,
# СЧИТАЕТ КОЛВО ПОВТОРЕНИЙ,
# ЗАПИСЫВАЕТСЯ В СЛОВАРЬ ПОД КЛЮЧЕМ С СООТВЕТСВУЮЩИМ ИМЕНЕМ,
# И ПЕРЕХОДИТ К СЛЕДУЩЕМУ ЭЛЕМЕНТУ


# ВАРИАНТ 3
# from collections import defaultdict
# word_count = defaultdict(int)

# for word in text_list:
#     print(word, word_count[word])
#     word_count[word] += 1
#
# ---- ВОПРОС К ВАРИАНТУ 3 ----
# 5. Самый топ варинат, как мне показалось, но опять же — как читается, что из себя представляет и так далее


print()
print('5) Вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).')
# чтобы отсортировать — нужно привести к списку
# но тогда не получится выбрать топ 5 значений и ключей

# следовательно нужно выбрать 5 топ ключей
# и как-то потом сопоставить со значениями


dict_text = {'все': '7', 'счастливые': '1', 'семьи': '4', 'похожи': '1', 'друг': '1', 'на': '10'}
for values in dict_text:
    val = list(dict_text.values())
    val.sort()
    val.reverse()
print(dict_text)












# def read_data(file_name):
# data = []
# with open(file_name, 'r', encoding='utf-8') as f:
# for line in f:
# parts = line.split()
# for item in parts:
# data.append(int(item))
# return data
#
# numbers = read_data('numbers.txt')
# print(numbers)
# print(sum(numbers))