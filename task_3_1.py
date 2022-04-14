def num_translate(number):
     num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
     return num_dict.get(number, 'None')

print(num_translate('five'))