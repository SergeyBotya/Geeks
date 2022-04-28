import os
import shutil

for root, dirs, files in os.walk(f'{os.path.dirname(os.path.abspath(__file__))}/my_project'):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            file_path_list = file_path.split('/')
            dir_path = os.path.join('my_project', 'templates', file_path_list[-2])
            new_file_path = os.path.join('my_project', 'templates', file_path_list[-2], file)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            shutil.copyfile(file_path, new_file_path)