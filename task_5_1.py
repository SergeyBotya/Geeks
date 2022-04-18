def num_generator(number):
    for i in range(1, number+1, 2):
            yield i


num_gen = num_generator(15)
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))