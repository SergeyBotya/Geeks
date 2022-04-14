def thesaurus(*args):
    names_dict = {}
    for i in range(0, len(args)):
        names_dict[args[i][0]] = names_dict.get(args[i][0], []) + [args[i]]
    print(names_dict)

thesaurus("Иван", "Олег", "Петя", "Игорь")