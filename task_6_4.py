import json
import sys

users = []
with open('users.csv', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.replace('\n', '')
        line = line.replace(',', ' ')
        users.append(line)
print(users)

hobbies = []
with open('hobby.csv', 'r', encoding='utf-8') as h:
    for line in h:
        line = line.replace('\n', '')
        line = line.replace(',', ', ')
        hobbies.append(line)
print(hobbies)

full_dict = {}
if len(users) == len(hobbies):
    for i in range(0, len(users)):
        full_users = users[i].split(' ')
        name = full_users[1]
        second_name = full_users[0]
        patronymic = full_users[2]
        full_dict[i] = {"фамилия": name, "имя": second_name, "отчество": patronymic, "хобби": hobbies[i]}
        with open('users_hobbies.txt', 'w', encoding='utf-8') as f:
            json.dump(full_dict, f)
elif len(users) > len(hobbies):
    last_users = users[len(hobbies):]
    users = users[:len(hobbies)]
    for i in range(0, len(users)):
        full_users = users[i].split(' ')
        name = full_users[1]
        second_name = full_users[0]
        patronymic = full_users[2]
        full_dict[i] = {"фамилия": name, "имя": second_name, "отчество": patronymic, "хобби": hobbies[i]}
    for j in range(0, len(last_users)):
        full_users = last_users[j].split(' ')
        name = full_users[1]
        second_name = full_users[0]
        patronymic = full_users[2]
        full_dict[j+(len(hobbies))] = {"фамилия": name, "имя": second_name, "отчество": patronymic, "хобби": "None"}
        with open('users_hobbies.txt', 'w', encoding='utf-8') as f:
            json.dump(full_dict, f)
else:
    sys.exit('1')






