'''Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.

Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
'''

num = input('Enter few nubmers: ').split()
print(sum(num.count(x) - 1 for x in num) // 2)

#another one

num = input('Enter few nubmers: ').split()
dct = {}

for element in num:
    dct[element] = dct.get(element, 0) + 1

output = sum(map(lambda element: sum(range(1, dct[element])), dct))

print("Pairs in the string: ", output)
