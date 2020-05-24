"""Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
   цена, а также количество S товара Посчитайте общую цену в рублях и копейках
   за L товаров.
"""


def total_sum(m, n, s):
    """Подсчет общей суммы покупок.

    :param m: рубли
    :param n: копейки
    :param s: количество товара
    :return: строка. общая цена в рублях и копейках. формат:
        'x rubles y kopecks'
    """
    m = int(input("Сколько рублей? "))
    n = int(input("Копеек: "))
    s = int(input("Введите сколько товара вы хотите: "))
    price_rub = m*s 
    price_coins = n*s
    #print("Общая цена: " + str(l1) + " рублей " + str(l2) + " копеек")
    return (str(price_rub) + " rubles " + str(price_coins) + " kopecks")  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s = '', '', ''
    print(total_sum(m, n, s))
