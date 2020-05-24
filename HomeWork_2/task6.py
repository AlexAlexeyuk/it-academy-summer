"""Определите, является ли число палиндромом (читается слева направо и справа
    налево одинаково).  Число положительное целое, произвольной длины. Задача
    требует работать только с числами (без конвертации числа в строку или
    что-нибудь еще)
"""


def palindrom(n):
    """Поиск числа фибоначчи.

    :param n: Число.
    :return: Bool. True или False. Является ли число палиндромом.
    """

    n1 = k = int(input("Enter any integer: "))
    n2 = 0

    while n1 > 0:
        left = n1 % 10; 
        n1 = n1 // 10; 
        n2 = n2 * 10 ;
        n2 = n2 + left ;
    if n2 == k:
        return True
    else:
        return False



if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 0
    print(palindrom(n))
