# инфа из доп источников

# Тернарный опертор Является способом записывать выражение присваивания в одну строку:
print('   Тернарный опертор Является способом записывать выражение присваивания в одну строку:')

value = 1 if (123**0.5) >= 10 else 0
#|___| |_| |______________|   |____|
#  |    |         |              |-> значение при невыполнении условия (обязательно)
#  |    |         |------------> условие
#  |    |-------------------------> значение при невыполнении условия
#  |-------------------------------> переменная, которой будет присвоено значение
print(value)



# Итератор списка
print('    Итератор списка list')

list_a = [x for x in range(0, 100) if x % 10 == 0]
#   |_|   |_|   |___________| |_____________|
#    |     |          |             |-> условие (не обязательный параметр)
#    |     |          |--------------> данная последовательность
#    |     |-------------------------> каждый элемент последовательности
#    |-------------------------------> целевая переменная (может быть выражение)
print(list_a)


# Итератор словаря
print('    Итератор словаря  dict')
dict_iter = {x: x*3 for x in range(0, 50) if x%10==0 }
#           |_||___|   |_|   |_________| |____________|
#           |    |     |          |             |-> условие (не обязательный параметр)
#           |    |     |          |--------------> данная последовательность
#           |    |     |------------------------> каждый элемент последовательности
#           |    |-------------------------------> целевая переменная (может быть выражение)
#           |-----------------------------------> ключ словаря
print(type(dict_iter), dict_iter)


# Итератор множеств
print('    Итератор множеств set')
set_iter = { x%3 for x in  range(0, 100) if x>=90 }
#           |_|        |_|    |__________|  |________|
#            |          |          |            |-> условие (не обязательный параметр)
#            |          |          |------------> данная последовательность
#            |          |-----------------------> каждый элемент последовательности
#            |------------------------------> целевая переменная (может быть выражение)
print(set_iter)

# Не пойму!!!     Не пойму!!!      Не пойму!!!


print('    Задача про имена в нижнем регистре')
''''

Задача. Дан список имен, первые символы которых необходимо
преобразовать верхний регистр.

isupper() - Состоит ли строка из символов в верхнем регистре
title() - Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний

'''

name_list = ['альфред', 'даниэль', 'милана'] # исходный список
title_name_list = [x if x.isupper() else x.title() for x in name_list] # целевой список
print(title_name_list)




# Лямбда-функция
print('    Лямбда-функция')

value = lambda x: 1 if x >= 10 else 0
#                |__________________|-> тело лямбда-функции
#|___|  |____||_||_||________| |____|
# |        |   |  |     |         |----> значение при невыполнении условия (обязательно)
# |        |   |  |     |------------> условие
# |        |   |  |-------------------> значение при невыполнении условия
# |        |   |----------------------> параметр функции
# |        |---------------------------> ключевое слово лямбда-функции
# |-----------------------------------> псевдоним лямда-функции!

print(value(1))






print()
# Лямбда-функции позволяют сокращать код. Например, имеется следующий код:
print('   Лямбда-функции позволяют сокращать код. Например, имеется следующий код:')

def fun(x):
 return x*x
def hot(x, fun):
 return x + fun

print(hot(3, fun(3)))

# сократим его с помощью лямбда-функций (возможно сделаем его менее понятным):
print('   сократим его с помощью лямбда-функций (возможно сделаем его менее понятным):')

hot = lambda x, fun: x + fun(x)
print(hot(3, lambda x: x*x))

''''
Лямбда-функция имеет следующие особенности:
- не может включать в тело некоторые операторы (return, pass, assert, raise)
- записывается в виде одной строки исполнения (можно разбивать с помощью круглых скобок)
- не поддерживает аннотации типов (нельзя явно указывать типы данных)
- немедленный вызов (например: (lambda x: x**2)(2)- без скобок вернется ссылка на объект)
- некорректная обработка исключений, т.к. нет имени
- поддерживает различные способы передачи аргументов (позиционные, именованные, переменный
                список, переменный список ключевых слов, аргументы только для ключевых слов)
- используется с функциями map(), filter(), reduce()

'''





print()
# Декораторы
print('    Декораторы   Декораторы   Декораторы   ')
''''
Декораторы
Являются функциями и предназначены для изменения поведения другой функций. Позволяет избавится
от необходимости изменения кода функций, поведение которых требуется изменить.
'''
import time
def show_time(f):     # --> декоратор
    def wrapper(*args, **kwargs):
        t = time.time()
        f(*args, **kwargs)
        print(f'{time.time() - t:.5f} сек.')
    return wrapper

@show_time  # --> генератор Генерирует список натуральных чисел в пределах num (+1!!!)
def int_gen_explicit(num = 1000000):
    for i in range(num):
        yield i + 1

@show_time    # --> итератор   Итерирует список натуральных чисел в пределах num (+1!!)
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


print()
# Сравнение объема потребляемой оперативной памяти для генератора и списка
print('    Сравнение объема потребляемой оперативной памяти для генератора и списка')

import os
import random
import psutil

''''
psutil (python system and process utilities) - является кросс-платформенной 
      библиотекой для получения информации о запущенных процессах 
      и использования системы (процессор, память, диски, сеть) в Python

Модуль os предоставляет множество функций для работы с операционной системой. 
     os.getpid() - текущий id процесса.    
    
'''
def show_proc(f):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        start = proc.memory_info().rss/1000000
        f(*args, **kwargs)
        proc = psutil.Process(os.getpid())
        stop = proc.memory_info().rss/1000000
        print(f'{stop-start} Мб.')
    return wrapper

@show_proc  # генератор
def int_gen_explicit(num = 1000000):
    for i in range(num):
        yield i + 1

@show_proc # итератор
def int_iter_explicit(num = 1000000):
    lst = []
    for i in range(num):
        lst.append(i+1)
    return lst

def time_difference():
    print(f'Объем потребляемой оперативной памяти для генератора составляет:')
    int_gen_explicit()
    print(f'Объем потребляемой оперативной памяти для создания списка составляет:')
    int_iter_explicit()
time_difference()





