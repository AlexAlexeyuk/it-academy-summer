def get_ranges(lst):
    """Реализовать функцию get_ranges.

    которая получает на вход непустой
    список неповторяющихся целых чисел,
    отсортированных по возрастанию, которая
    этот список “сворачивает”
     get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
     get_ranges([4,7,10]) // "4,7,10"
     get_ranges([2, 3, 8, 9]) // "2-3,8-9"
    """

    list_1 = []
    list_2 = []
    for el in range(len((lst))):
        if el + 1 < len(lst) and lst[el] == lst[el + 1] - 1:
            list_2.append(lst[el])
        else:
            list_2.append(lst[el])
            list_1.append(list_2.copy())
            list_2.clear()

    result = []
    for elem in list_1:
        if len(elem) > 1:
            result.append("{}-{}".format(elem[0], elem[-1]))
        else:
            result.append(str(elem[0]))

    return ",".join(result)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
