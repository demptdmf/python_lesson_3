f = open('text.txt')
text = f.read()

'''1) методами строк очистить текст от знаков препинания;'''
symbols = ['.', ',', ';', ':', '!', '?', '«', '»', '—']
for symbols in symbols:
    text = text.replace(symbols, '')
print()

'''2) сформировать list со словами (split);'''
text_list = list(text.split())
print(text_list)
print(type(text_list))
print()


'''3) привести все слова к нижнему регистру (map);'''
text_list = list(map(lambda letters: letters.lower(), text_list))
print(text_list)
print(len(text_list), type(text_list))
print()


'''4) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;'''
dict_text = {}                                  # Создаем пустой словарь
for word in text_list:                          # В ЦИКЛЕ БЕРЕТСЯ ПЕРВОЕ СЛОВО, ОБХОДИТСЯ ПО СПИСКУ,
    dict_text[word] = text_list.count(word)     # СЧИТАЕТСЯ КОЛ-ВО ПОВТОРЕНИЙ, ЗАПИСЫВАЕТСЯ В СЛОВАРЬ ПОД КЛЮЧЕМ С СООТВЕТСВУЮЩИМ ИМЕНЕМ И ПЕРЕХОДИТ К СЛЕДУЩЕМУ ЭЛЕМЕНТУ
print(dict_text)
print(len(dict_text))
print()
'''ДЛЯ СЛОВА В СПИСКЕ ЗАПИСЫВАТЬ В СЛОВАРЬ СЛОВО С КОЛИЧЕСТВОМ ПОВТОРЕНИЙ ЭТОГО СЛОВА В СПИСКЕ'''


'''5) вывести 5 наиболее часто встречающихся слов (sort)'''
text_list = list(dict_text.items())
text_list.sort(key=lambda i: i[1])
text_list.reverse()
print(text_list[:5])
print()

'''вывести количество разных слов в тексте (set).'''

print(len(text_list), '— элементов в списке')
print(len(set(text_list)), '— элементов в множестве')

similar_count = 0
for value in dict_text.values():
    if value == 1:
        similar_count += 1
print(similar_count, '— одинаковых слов')

different_count = 0
for value in dict_text.values():
    if value > 1:
        different_count += 1
print(different_count, '— разных слов')


)