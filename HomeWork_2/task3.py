"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все
    пробелы. Например, если было введено "abc cde def", то должно быть
    выведено "abcdef".

   Подсказка: оператор in проверяет, входит ли подстрока в строку или нет.
"""

def sub_string(str_):
    """Конструирование подстроки.

    :param str_: входная строка
    :return: строка. Получившееся выражение
    """

    str_ = input("Enter any string: ")
    l = []
    n = []
    for i in str_:
        if i !=" ":
            l.append(i)
            for r in l:
                if r not in n:
                    n.append(r)

    return ("You get a string without any spaces and repeats: " + ''.join(n))



if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(sub_string(str_))
