task_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lines = line.split(' ')
        task_tuple = (lines[0], lines[5][1:], lines[6])
        task_list.append(task_tuple)
print(task_list)