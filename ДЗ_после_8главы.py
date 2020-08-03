# ДЗ после 8 главы

# 1. Написать декоратор, замеряющий время выполнение декорируемой функции.
print('    1. Написать декоратор, замеряющий время выполнение декорируемой функции.')

import time
def dec_time(f):  # декоратор
    def func(*args, **kwargs):
        t=time.time()
        f()
        print('Время работы декоратора составляет: ' + f'{time.time()-t:.5f} сек.')
    return func

@dec_time
def time_measurement(num=1000000):
    lst=[]
    for i in range(num):
        lst.append(i+1)
    return lst

time_measurement()


print()
# 2. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).
print('    2. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).')


def show_time(f):
    def wrapper(*args, **kwargs):
        t = time.time()
        f(*args, **kwargs)
        print(f'{time.time() - t:.5} сек.')
    return wrapper

@show_time
def gen_numb(num = 100000):
    for i in range(num):
        yield i + 1

@show_time
def iter_numb(num = 100000):
    lst=[]
    for i in range(num):
        lst.append(i+1)
    return lst


def time_difference():
    print(f'Время работы генератора составляет: ')
    gen_numb()
    print(f'Время работы функции по созданию списка составляет: ')
    iter_numb()

time_difference()






print()
# 3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
print('    3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.')

import os
import psutil




def dec_ram(f):  # декоратор
    def func_ram(*args, **kwargs):
        ram = psutil.Process(os.getpid())
        print('Объем используемой оперативной памяти в начале выполнения кода составляет: ' + str(ram.memory_info().rss/1000000))

        f()

        ram_2 = psutil.Process(os.getpid())
        print('Объем используемой оперативной памяти в конце выполнения кода составляет: ', str(ram_2.memory_info().rss/1000000))
    return func_ram()

@dec_ram
def ram_measurement(num_r=1000000):
    lst=[]
    for i in range(num_r):
        lst.append(i+1)
    return lst

ram_measurement




print()
# 4. Сравнить объем оперативной памяти для функции создания генератора и функции создания списка с элементами: натуральные числа от 1 до 1000000.
print('    4. Сравнить объем оперативной памяти для функции создания генератора и функции создания списка с элементами: натуральные числа от 1 до 1000000.')




def show_ram_gen_iter(f):
    def wrapper(*args, **kwargs):
        ram = psutil.Process(os.getpid())
        start_ram = ram.memory_info().rss/1000000

        f(*args, **kwargs)

        ram = psutil.Process(os.getpid())
        stop_ram = ram.memory_info().rss/1000000
        print(f'{stop_ram - start_ram:.5f} Мб.')
    return wrapper

@show_ram_gen_iter #Генератор
def gen_numb(num):
    for i in range(num):
        yield i + 1

@show_ram_gen_iter #Итератор
def iter_numb(num):
    lst = []
    for i in range(num):
        lst.append(i+1)
    return lst

def ram_difference(n):
    print(f'Объем потребляемой оперативной памяти для генератора составляет:')
    gen_numb(n)
    print(f'Объем потребляемой оперативной памяти для итератора составляет:')
    iter_numb(n)

ram_difference(1000000)


