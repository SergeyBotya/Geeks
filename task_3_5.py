nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(a, flag):
    import random, copy
    jokes = []
    nouns_copy = copy.deepcopy(nouns)
    adverbs_copy = copy.deepcopy(adverbs)
    adjectives_copy = copy.deepcopy(adjectives)
    i = 1
    if flag == True:
        if a > len(nouns_copy):
            print('Перезапустите программу, введите корректное число шуток')
        else:
            while i <= a:
                noun = random.choice(nouns_copy)
                nouns_copy.remove(noun)
                adverb = random.choice(adverbs_copy)
                adverbs_copy.remove(adverb)
                adjective = random.choice(adjectives_copy)
                adjectives_copy.remove(adjective)
                jokes += [f'{noun} {adverb} {adjective}']
                i += 1
            print(jokes)
    else:
        while i <= a:
            jokes += [f"{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}"]
            i += 1
        print(jokes)


get_jokes(5, True)