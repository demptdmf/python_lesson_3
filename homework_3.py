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
# 2. Появились двойные пробелы благодаря этой очистке. Ошибки в этом нет, т.к. шло 3 символа подряд, но как убрать двойные пробелы? text = text.replace('  ', '') ?

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

# ВАРИАНТ 1

text_dict = {}
dict = new_list
for i in list(dict):
    counts = 0
    while i in list(dict):
        if i in list(dict):
            counts += 1
            dict.remove(i)
            text_dict[i] = counts
print(text_dict)

# ---- ВОПРОС К ВАРИАНТУ 1 ----
# Подсмотрел у одного студента в комментариях это решение
# 3. Как оно читается? Не понимаю, потому что очень замудренное кажется.


# ВАРИАНТ 2
text_dict = {}
for i in range(len(new_list)):
    text_dict[new_list[i]] = new_list.count(new_list[i])
print(text_dict)

# ---- ВОПРОС К ВАРИАНТУ 2 ----
# Тоже подсмотрел, но не работает(
# 4. Почему не работает и как оно читается хочется понять преимущественно, т.к. этот код более короткий с одним правильным циклом










# если скопировать значение листа и присвоить ему dict — то пишет ошибку (даже если это значание закомментировано):
# SyntaxError: Non-UTF-8 code starting with '\xd0' in file homework_3.py on line 28, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
# Искал в интернете решение — предложили import collections, но там слова даны в str, это значит нужно привести к листу

        # from collections import defaultdict
        # word_count = defaultdict(int)
        # for word in text:
        #     print(word, word_count[word])
        #     word_count[word] += 1


# print('5) Вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).')





















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