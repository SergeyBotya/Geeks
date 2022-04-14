def thesaurus_adv(*args):
    names_dict = {}
    for i in range(0, len(args)):
        surname = args[i].split()
        names_dict[surname[1][0]] = names_dict.get(surname[1][0], []) + [args[i]]
    for key, val in names_dict.items():
        full_names = {}
        for j in range(0, len(val)):
            full_names[val[j][0]] = full_names.get(val[j][0], []) + [val[j]]
        names_dict[key] = full_names
    return names_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
