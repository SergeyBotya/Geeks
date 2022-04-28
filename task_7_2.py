import os

dirs = ['settings', 'mainapp', 'authapp']
files_1 = ['--__init__.py', 'dev.py', 'prod.py']
files_2 = ['--__init__.py', 'models.py', 'views.py']
dirs_2 = ['templates', 'mainapp']
files_2_2 = ['base.html', 'index.html']
files_3 = ['__init__.py', 'models.py', 'views.py']
dirs_3 = ['templates', 'authapp']
files_3_2 = ['base.html', 'index.html']
for directory in dirs:
    dir_path = os.path.join('my_project', directory)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        if directory == dirs[0]:
            for file in files_1:
                file_path = os.path.join('my_project', directory, file)
                if not os.path.exists(file_path):
                    f = open(f'{dir_path}/{file}', 'w+')
                    f.close()
        if directory == dirs[1]:
            for file in files_2:
                file_path = os.path.join('my_project', directory, file)
                if not os.path.exists(file_path):
                    f = open(f'{dir_path}/{file}', 'w+')
                    f.close()
            dir_path = os.path.join('my_project', directory, dirs_2[0], dirs_2[1])
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            for file in files_2_2:
                file_path = os.path.join('my_project', directory, dirs_2[0], dirs_2[1], file)
                if not os.path.exists(file_path):
                    f = open(f'{dir_path}/{file}', 'w+')
                    f.close()
        if directory == dirs[2]:
            for file in files_3:
                file_path = os.path.join('my_project', directory, file)
                if not os.path.exists(file_path):
                    f = open(f'{dir_path}/{file}', 'w+')
                    f.close()
            dir_path = os.path.join('my_project', directory, dirs_3[0], dirs_3[1])
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            for file in files_3_2:
                file_path = os.path.join('my_project', directory, dirs_3[0], dirs_3[1], file)
                if not os.path.exists(file_path):
                    f = open(f'{dir_path}/{file}', 'w+')
                    f.close()