import time
import os
import random
import psutil

def show_proc(f):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        start = proc.memory_info().rss/1000000
        f(*args, **kwargs)
        proc = psutil.Process(os.getpid())
        stop = proc.memory_info().rss/1000000
        print(f'{stop-start:.5f} Mb.')
    return wrapper

@show_proc
# генератор
def int_gen_explicit(num):
    for i in range(num):
        yield i + 1



@show_proc
# итератор
def int_iter_explicit(num):
    lst = []
    for i in range(num):
        lst.append(i+1)
    return lst

def time_difference(n):
    print(f'Объем потребляемой оперативной памяти для генератора составляет:')
    int_gen_explicit(n)
    print(f'Объем потребляемой оперативной памяти для создания списка составляет:')
    int_iter_explicit(n)

#print('Исп. память до вып. функции:' + str(proc.memory_info().rss/1000000))
time_difference(1000000)
#proc=psutil.Process(os.getpid())
#print('Исп. память после вып. функции:'+str(proc.memory_info().rss/1000000))