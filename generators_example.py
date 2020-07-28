# 8.3. Генераторы

'''
ПЛОХО   ПЛОХО   ПЛОХО   ПЛОХО   ПЛОХО   ПЛОХО   ПЛОХО   ПЛОХО   ПЛОХО

!!! Почему у нас в лекциях ошибки и их ни кто не освещает, не исправляет
часть где: 
Создадим список машиноцветов, 
помереем обьем памяти....

Используются
start=time.clock() # Засекаем время
stop=time.clock() # время после кода
print('Используемая память полсе вып.фун-ции: ', str(proc.memory_info().rss/1000000))
print("Заняло {} секунд: ".format(stop-start)) # сколько времени заняло выполнение функции

У меня этот код не работает.



 Возможно стоит записать урок на чистовик?

'''



#Почувствем разницу между негерторами списков и просто генераторами
print('    Почувствем разницу между негерторами списков и просто генераторами')

import sys # будем измерять обьем памяти

simple_list = [x**3 for x in range(5)]
print(type(simple_list))

for i in simple_list:
    print(i)
print('обьем памяти simple_list: ',sys.getsizeof(simple_list)) # Проверим обьем занимаемой памяти


# Неявные генераторы ( задаются с помощью круглых скобок)
print('   Неявные генераторы ( задаются с помощью круглых скобок)')

'''
Неявный, по  тому, что очень простой,
в нем не использованиы какие то особые сво-ва генераторов
'''

simple_generator = (x**3 for x in range(5))
print(type(simple_generator))


for i in simple_generator:
    print(i)
print('обьем памяти simple_generator: ',sys.getsizeof(simple_generator)) # Проверим обьем занимаемой памяти


print()
'''
Для большего понимания, разницы в щанимаемой памяти
я проделаю тоже самое, но диапазон изменю с 5 на 100.
Выводить сами числа (кубы) не буду

'''
print('    Измерим обьем памяти при ранж 100')

simple_list_100 = [x**3 for x in range(100)]
print(type(simple_list_100))
print('обьем памяти simple_list_100: ',sys.getsizeof(simple_list_100)) #  обьем занимаемой памяти при 100

simple_generator_100 = (x**3 for x in range(100))
print(type(simple_generator_100))
print('обьем памяти simple_generator_100: ',sys.getsizeof(simple_generator_100)) # обьем занимаемой памяти при 100
'''
Мы увиди, что в листе весь обьем хранится в памяти
а в генераторе нет.

Генератор каждый раз вычисляет новы элемент
ему не нужно хрантиь это все  в памяти

'''

print()
# ЯВНЫЕ генераторы, простой пример
print('    ЯВНЫЕ генераторы, простой пример')

def generator_example_1(num): # num это количество генераторов которые мы хотим создать
    for i in range(num):
        yield (i**3)
gen = generator_example_1(10)

print('1 запрос: ', next(gen)) # next ключевое слово, для получения следующих элементов
print('2 запрос: ',next(gen))
print('3 запрос: ',next(gen))
print('4 запрос: ',next(gen))


print()
# ЯВНЫЕ генераторы, сложный пример
print('    ЯВНЫЕ генераторы, сложный пример')

'''
Создадим список машиноцветов, 
помереем обьем памяти 
и время которое необходимо для обхода полученного списка

'''
import time
import os
import random
import psutil

colors = ['White', 'Black', 'Green']
brands = ['Volvo', 'Lada', 'Audi']

'''
Я задокстринил эту часть кода, т.к. это влияет на обьем памяти 
в следующем коде

def cars(num):
    cars_list = []
    for i in range(num):
        car = {'Цвет':random.choice(colors),
               'Марка':random.choice(brands),
               'id':i}
        cars_list.append(car)
    return cars_list

proc = psutil.Process(os.getpid()) # помереем используемую до выполнения память
print('Используемая память до вып.фун-ции: ', str(proc.memory_info().rss/1000000)) # memory_info - это вычисление памяти., в атрибуте rss хранится текущее значение используемое количество памятив кэше

time_1 = time.time()
#start_time = time.localtime()
#start=time.clock() # Засекаем время
cars_list=cars(1000000) # Создаем список из 1 млн. обьектов
#stop=time.clock() # время после кода
end_time = time.localtime()

proc =psutil.Process(os.getpid()) # измеряем память после выполнения
print('Используемая память полсе вып.фун-ции: ', str(proc.memory_info().rss/1000000))

#print("Заняло {} секунд: ".format(stop-start)) # сколько времени заняло выполнение функции
#time_period = (end_time-start_time)
elapsed_time = time.time() - time_1
print('Время исполнения кода: ', elapsed_time)
#print(time_period)
'''

print()
# Теперь тоже самое, но с использованием генератора
print('   Теперь тоже самое, но с использованием генератора')

def cars_gen(num):
    for i in range(num):
        car = {'Цвет':random.choice(colors),
               'Марка':random.choice(brands),
               'id':i}
        yield car

proc_gen = psutil.Process(os.getpid()) # помереем используемую до выполнения память
print('Используемая память до вып.фун-ции: '+str(proc_gen.memory_info().rss/1000000)) # memory_info - это вычисление памяти., в атрибуте rss хранится текущее значение используемое количество памятив кэше

time_1_gen = time.time()
#start_time = time.localtime()
#start=time.clock() # Засекаем время
cars_list_gen=cars_gen(1000000) # Создаем список из 1 млн. обьектов
#stop=time.clock() # время после кода
#end_time_gen = time.localtime()
time_2_gen = time.time()
proc_gen =psutil.Process(os.getpid()) # измеряем память после выполнения

print('Используемая память полсе вып.фун-ции: '+str(proc_gen.memory_info().rss/1000000))

print("Время исполнения кода: {} секунд".format(time_1_gen-time_2_gen )) # сколько времени заняло выполнение функции




