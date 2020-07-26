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

# продолжить с 11 минуты