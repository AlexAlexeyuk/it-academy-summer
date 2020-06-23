def count_letters(str_):
    
"""Подсчет символов.:param str_: входная строка
:return: кортеж. (low_number, up_number).
low_number - количество строчных,
up_number - количество пописных."""

    str_ = input("Enter any string: ")
    low_number = 0
    up_number = 0
    for i in str_:
        if 'a' <= i <= 'z':
            low_number += 1
        else:
            if 'A' <= i <= 'Z':
                up_number += 1
    return (low_number, up_number)

if __name__ == '__main__':
    str_ = ''
    print(count_letters(str_))
