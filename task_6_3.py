import json
import sys
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users_file:
    content = users_file.read()
    users = content.splitlines()

with open('hobby.csv', 'r', encoding='utf-8') as hobby_file:
    content = hobby_file.read()
    hobbies = content.splitlines()

if len(users) >= len(hobbies):
    users_dict = {key: val for key, val in zip_longest(users, hobbies, fillvalue="None")}
    print(users_dict)
    with open('users_hobbies.txt', 'w', encoding='utf-8') as f:
        json.dump(users_dict, f)
else:
    sys.exit('1')



