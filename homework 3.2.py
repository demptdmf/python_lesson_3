'''Самое короткое и красивое решение'''
f = open('text.txt')
text = f.read()

symbols = ['.', ',', ';', ':', '!', '?', '«', '»', '—']
for symbols in symbols:
    text = text.replace(symbols, '')
print()

text = text.lower()
text = text.split()
print(text)
print()

dict_ = {}
for word in text:
    dict_[word] = text.count(word)
dict_tolist = list(dict_.items())
print('Количество повторений слов:', dict_tolist)

dict_tolist.sort(key=lambda i: i[1], reverse = True)
top_five = dict_tolist[0:5]
print('Пять самых частых слов: ', top_five)

words_set = set(text)
words_quantity = len(words_set)
print('Количество разных слов:', words_quantity)