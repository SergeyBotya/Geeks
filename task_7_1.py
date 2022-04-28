import os

dirs = ['settings', 'mainapp', 'adminapp', 'authapp']

for directory in dirs:
    dir_path = os.path.join('my_project', directory)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)