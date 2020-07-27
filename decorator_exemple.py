# 8.2. Декораторы

# Простой декоратор
print('   Простой декоратор    Простой декоратор')
def show_information(f):  # Классичесский декоратор
    def wrapper():
        print('Код до функции!')
        f()
        print('Код после функции')
    return wrapper


def simple_function():
    print('Я простая функция')


# просто сначала проверим нашу функцию
print('  просто сначала проверим нашу функцию')
simple_function()


# теперь используем декоратор show_information(f)
print('   теперь используем декоратор show_information(f)')

simple_function_decoration = show_information(simple_function)
simple_function_decoration()

print('  *   *')
'''' 
Но это все неудобно, это плодит не нужные сущности в программе, 
напр simple_function_decoration.
Создадим новую ф-ю 

'''
@show_information # это декоратор, обертка
def another_simple_function():
    print('Я тоже простая функция.')
another_simple_function()

print()
# Декораторы с параметрами
print('   - Декораторы с параметрами -')

def show_type(f):

    def wrapper(*args, **kwargs):
        print('2_Код до функции!')
        print(f(*args, **kwargs))
        print('2_Код после функции')
    return wrapper

@show_type
def my_add(a,b):
    return a+b
my_add(10, 20)

# Тоже самое, но с type
print('   - - Тоже самое, но с type')
def show_type(f):

    def wrapper(*args, **kwargs):
        print('Код до функции type!', type(args[0]))
        print(f(*args, **kwargs))
        print('Код после функции type', type(args[1]))
    return wrapper


@show_type
def my_add(a,b):
    return a+b
my_add(10, 20)


print()
print('   - * * - Тоже самое, но с type + навесим два декоратора. Каскадная модель декораторов')

def show_information(f):  # Классичесский декоратор
    def wrapper(*args, **qwargs):
        print('Код до функции +2 !')
        f(*args, **qwargs)
        print('Код после функции +2')
    return wrapper

def show_type(f):

    def wrapper(*args, **kwargs):
        print('Код до функции type!', type(args[0]))
        print(f(*args, **kwargs))
        print('Код после функции type', type(args[1]))
    return wrapper




@show_information
@show_type
def my_add(a,b):
    return a+b
my_add(40, 20)



print()
# Вывод времени
print('   # Вывод времени   # Вывод времени')

import time
import requests

def show_time(f):

    def wrapper(*args, **kwargs):
        print(time.time())
        print('URL: ', args[0])
        print(f(*args, **kwargs))
        print(time.time())
    return wrapper

@show_time
def requests_example(url):
    webpage = requests.get(url)
    return webpage.text

url = 'https://www.google.com'

requests_example(url) # Проверим, что делает эта функция