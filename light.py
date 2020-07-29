import time

def show_time(f):
    def wrapper(*args, **kwargs):
        t = time.time()
        f(*args, **kwargs)
        print(f'{time.time() - t:.5f} сек.')
    return wrapper

@show_time
# генератор
def int_gen_explicit(num = 1000000):
    for i in range(num):
        yield i + 1

@show_time
# генератор
def int_iter_explicit(num = 1000000):
    lst = []
    for i in range(num):
        lst.append(i+1)
    return lst

def time_difference():
    print(f'Время работы генератора составляет:')
    int_gen_explicit()
    print(f'Время работы функции по созданию списка составляет:')
    int_iter_explicit()

time_difference()