#Создаём список
main_list = []

for i in range(1, 1000):
    if i % 2 != 0:
        main_list.append(i ** 3)
print(f'Список чисел: {main_list} \n')
# \n добавил для удобства читаемости вывода

#Вычесляем сумму
main_sum_a = 0
for number_a in main_list:
    sum_number_a = 0  # переменная суммы чисел в числе строки
    number_a_string = str(number_a)
    j = 0
    while j < len(number_a_string):
        sum_number_a += int(number_a_string[j])
        j += 1
    if sum_number_a % 7 == 0:
        main_sum_a += number_a
print(f'Сумма чисел: {main_sum_a} \n')

#Прибавляем 17 к каждому числу в списке и пересчитываем сумму
main_sum_b = 0
for number_b in main_list:
    sum_number_b = 0
    number_b_string = str((number_b) + 17)
    k = 0
    while k < len(number_b_string):
        sum_number_b += int(number_b_string[k])
        k += 1
    if sum_number_b % 7 == 0:
        main_sum_b += int(number_b_string)
print(f'Новая сумма чисел: {main_sum_b}')















