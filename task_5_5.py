from time import perf_counter
import sys

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start_1 = perf_counter()
first_method = [a for a in src if src.count(a) == 1]
print(first_method, perf_counter() - start_1, sys.getsizeof(first_method))

start_2 = perf_counter()
second_method = set()
src_2 = set()
for b in src:
    if b not in src_2:
        second_method.add(b)
    else:
        second_method.discard(b)
    src_2.add(b)
second_method = [b for b in src if b in second_method]
print(second_method, perf_counter() - start_2, sys.getsizeof(second_method))

