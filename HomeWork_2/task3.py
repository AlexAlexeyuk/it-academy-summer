"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все
    пробелы. Например, если было введено "abc cde def", то должно быть
    выведено "abcdef".   Подсказка: оператор in проверяет, 
    входит ли подстрока в строку или нет.
"""
def sub_string(str_):
    """Конструирование подстроки.
    :param str_: входная строка
    :return: строка. Получившееся выражение
    """
    str_ = input("Enter any string: ")
    list_1 = []
    list_2 = []
    for i in str_:
        if i !=" ":
            list_1.append(i)
    for i in list_1:
        if i not in list_2:
            List_2.append(i)
    return ("You get a string without any spaces and repeats: " + ''.join(list_2))
if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(sub_string(str_))
