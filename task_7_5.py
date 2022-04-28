import os

task_tuple = {}
extensions_list_100 = []
extensions_list_1000 = []
extensions_list_10000 = []
extensions_list_100000 = []
for root, dirs, files in os.walk(f'{os.path.dirname(os.path.abspath(__file__))}/some_data'):
    size_100 = [file for file in files if os.stat(os.path.join(root, file)).st_size < 100]
    for file_name in size_100:
        extension = file_name.split('.')
        if extension[-1] not in extensions_list_100:
            extensions_list_100.append(extension[-1])
    task_tuple[100] = (len(size_100), extensions_list_100)
    size_1000 = [file for file in files if 1000 > os.stat(os.path.join(root, file)).st_size > 100]
    for file_name in size_1000:
        extension = file_name.split('.')
        if extension[-1] not in extensions_list_1000:
            extensions_list_1000.append(extension[-1])
    task_tuple[1000] = (len(size_1000), extensions_list_1000)
    size_10000 = [file for file in files if 10000 > os.stat(os.path.join(root, file)).st_size > 1000]
    for file_name in size_10000:
        extension = file_name.split('.')
        if extension[-1] not in extensions_list_10000:
            extensions_list_10000.append(extension[-1])
    task_tuple[10000] = (len(size_10000), extensions_list_10000)
    size_100000 = [file for file in files if 100000 > os.stat(os.path.join(root, file)).st_size > 10000]
    for file_name in size_100000:
        extension = file_name.split('.')
        if extension[-1] not in extensions_list_100000:
            extensions_list_100000.append(extension[-1])
    task_tuple[100000] = (len(size_100000), extensions_list_100000)
print(task_tuple)