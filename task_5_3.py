# Сделал для трех случаев. Когда списки равны по кол-ву эл-ов, и два варианта, когда один длинее другого.

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
if len(tutors) == len(klasses):
        new_tuple = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
        i = 1
        while i <= len(tutors):
            print(next(new_tuple))
            i += 1
        print(type(new_tuple))
elif len(tutors) < len(klasses):
    last_klasses = klasses[len(tutors):]
    klasses = klasses[0: len(tutors)]
    new_tuple = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
    i = 1
    while i <= len(tutors):
        print(next(new_tuple))
        i += 1
    i = 0
    while i < len(last_klasses):
        last_tuple = (None, last_klasses[i])
        print(last_tuple)
        i += 1
    print(type(new_tuple))
else:
    last_tutors = tutors[len(klasses):]
    tutors = tutors[0:len(klasses)]
    new_tuple = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
    i = 1
    while i <= len(klasses):
        print(next(new_tuple))
        i += 1
    i = 0
    while i < len(last_tutors):
        last_tuple = (last_tutors[i], None)
        print(last_tuple)
        i += 1
    print(type(new_tuple))

