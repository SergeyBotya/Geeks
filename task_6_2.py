stop_spam = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lines = line.split(' ')
        stop_spam.append(lines[0])

# Первый вариант решения. В две строчки, но ноут сильно греется и долго думает
spam_ip = max(stop_spam, key=stop_spam.count)
print(f'API: {spam_ip} обращался {stop_spam.count(spam_ip)} раз')

# Второй вариант решения выглядит более оптимизированным
new_stop_spam = []
for i in range(len(stop_spam)):
    if stop_spam[i] not in new_stop_spam:
        new_stop_spam.append(stop_spam[i])

spammer = {}
for k in new_stop_spam:
    j = stop_spam.count(k)
    spammer[k] = j
spam_ip = (max(spammer, key=spammer.get))
print(f'API: {spam_ip} обращался {spammer[spam_ip]} раз')
