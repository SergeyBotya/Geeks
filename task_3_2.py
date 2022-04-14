def num_translate(number):
    num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if number == number.title():
        return num_dict[number.lower()].title()
    else:
        return num_dict[number]

print(num_translate('zero'))