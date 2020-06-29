def sub_string(str_):


    """Конструирование подстроки.
    
    :param str_: входная строка
    :return: строка. Получившееся выражение
    """

    str_ = input("Enter any string: ")
    list_1 = []
    list_2 = []
    for i in str_:
        if i != "":
            list_1.append(i)
    for i in list_1:
        if i not in list_2:
            list_2.append(i)
    return ("You get a string without any spaces and repeats: " + ''.join(list_2))

if __name__ == '__main__':
    str_ = ''
    print(sub_string(str_))
