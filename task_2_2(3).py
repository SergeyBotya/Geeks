main_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
'была', '+5', 'градусов']

for i in range(len(main_list)-1, 0, -1):
    try:
        if type(int(main_list[i])) == int:
            main_list[i] = main_list[i].zfill(2)
            main_list.insert(i + 1, '"')
            main_list.insert(i, '"')

    except ValueError:
        pass
print(*main_list)