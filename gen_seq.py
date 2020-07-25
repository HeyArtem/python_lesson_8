# 8.1. Тернарный оператор

age = 25

def chek_adult(age):
    chek = 0
    if age >= 18:
        chek = 1
    else:
        chek = 0
    return chek

#print(chek_adult(age))


# Перепишем с помощью тернарного оператора
print('   Перепишем с помощью тернарного оператора')

#age = 25
chek = 1 if age >= 18 else 0
#print(chek)

# или с помощью lambda
print('   или с помощью lambda')

chek_adult_lambda = lambda x: 1 if age >= 18 else 0


print(chek_adult(age), chek, chek_adult_lambda(age))




#   * * Генераторы последовательностей. СПИСОК   СПИСОК    * *
print('   * * Генераторы последовательностей. СПИСОК   СПИСОК    * * ')

# Сгенерируем список из квадратов чисел
print('   Сгенерируем список из квадратов чисел')

list_sq = []
N = 10 # количество требуемых квадратов

for i in range(1, N+1):
    list_sq.append(i**2)
print(list_sq)



# Генераторы последовательностей
print('     Генераторы последовательностей')

# Сгенерируем остатки от деления на 10
print('    Сгенерируем остатки от деления на 10')

list_sq_division = []
for i in range(1, N+1):
    list_sq_division.append((i**2)%10)
print(list_sq_division)



# Теперь сгенерируем с помощью генераторов списков
print('   Теперь сгенерируем с помощью генераторов списков')

list_sq_division_g = [(i**2)%10 for i in range(1, N+1)]
print(list_sq_division_g)





# Громоздкость кода увеличивается если добавляется if
print('   Громоздкость кода увеличивается если добавляется if')
list_sq_division_гром = []
for i in range(1, N+1):
    if (i**2)%2 == 0:
        list_sq_division_гром.append(i**2)
print(list_sq_division_гром)

# Громоздкость (if) с помощью генераторов списков
print('   Громоздкость (if) с помощью генераторов списков')
list_sq_division_g_гром = [i**2 for i in range(1, N+1) if (i**2)%2==0] # -> Это ПИТОНОВСКИЙ стиль (короче и наверно быстрей, узнаем из домашки)
print(list_sq_division_g_гром)




# Генератор словаря
print('    Генератор словаря')









#   *  Генераторы последовательностей. СЛОВАРЬ   СЛОВАРЬ   *
print('   *  Генераторы последовательностей. СЛОВАРЬ   СЛОВАРЬ   *  ')
dict_q = {i:i**2 for i in range(1, N+1) }
print(dict_q)





#   *-*  Генераторы последовательностей. МНОЖЕСТВО   МНОЖЕСТВО      *-*
print('   *-*  Генераторы последовательностей. МНОЖЕСТВО   МНОЖЕСТВО      *-*')
set_q = {i**2 for i in range(1, N+1) }
set_q_dinision = {(i**2)%10 for i in range(1, N+1) }
print(set_q, set_q_dinision)



print()
# Задача     Задача
print('   Задача     Задача    Задача     Задача    ')

#    Сформировать список из первых букв, но так, что бы они были заглавные
print('   Сформировать список из первых букв, но так, что бы они были заглавные')

list_names = ['Dima', 'kate', 'Oleg', 'natali']

list_char = [ x[0] if x[0].isupper() else x[0].title() for x in list_names]  # Мы использовали ф-ю  Тернарный оператор и Генератор списка
print(list_char)