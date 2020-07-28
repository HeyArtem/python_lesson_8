# 8.3. Генераторы. Код с ошибками из лекций

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

def cars(num):
    cars_list = []
    for i in range(num):
        car = {'colocr':random.choice(colors),
               'brand':random.choice(brands),
               'id':i}
        cars_list.append(car)
    return cars_list

proc = psutil.Process(os.getpid())
print('Используемая память до вып.фун-ции:'+str(proc.memory_info().rss/1000000))

start=time.clock() # !
cars_list = cars(1000000)
stop=time.clock() # !

proc=psutil.Process(os.getpid())
print('Исп. память полсе вып.фун-ции:'+str(proc.memory_info().rss/1000000))

print("Заняло {} секунд".format(stop-start)) # !
