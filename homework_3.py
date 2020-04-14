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
text = text.replace('—', '')    # Хотел сделать в единой строке через or/and/& — но все условия не выполнялись. Сделал вручную, можно как-то сразу всё?
print(text)                     # Появились двойные пробелы благодаря этой очистке. Ошибки в этом нет, т.к. шло 3 символа подряд, но как убрать двойные пробелы?
print()


print('2) Сформировать list со словами (split):')
text = text.split()
print(type(text))
print()


print('3) Gривести все слова к нижнему регистру (map);')
text = list(map(lambda x: x.lower(), text))
print(text)
print()


print('4) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;')
# если скопировать значение листа и присвоить ему dict — то пишет ошибку:
# SyntaxError: Non-UTF-8 code starting with '\xd0' in file homework_3.py on line 28, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details





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