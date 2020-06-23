from collections import Counter

'''Дан список. Выведите те его элементы, которые встречаются в списке
только один раз. Элементы нужно выводить в том порядке, 
в котором они встречаются в списке.'''

list_ = [1, 'a', 1, 'a', 'b']
c = Counter(list_)
list_1 = [x for x in list_ if c[x] == 1]
print(list_1)


# second variant to solve that
input_list = ['a', 1, 2, 2, 3, 3, 4, 4, 5, 6]
list_res = []
dict_ = {}
for i in input_list:
    dict_[i] = dict_.get(i, 0) + 1
    if dict_.get(i) == 1:
        list_res.append(i)
print('Unique elements in input list: ', list_res)
