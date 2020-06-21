def total_sum(m, n, s):
   
    """Подсчет общей суммы покупок.
    :param m: рубли
    :param n: копейки
    :param s: количество товара
    :return: строка. общая цена в рублях и копейках. 
    формат:'x rubles y kopecks'
    """
    m = int(input("Сколько рублей? "))
    n = int(input("Копеек: "))
    s = int(input("Введите сколько товара вы хотите: "))
    return (str(m*s) + " rubles " + str(n*s) + " kopecks") 

if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s = '', '', ''
    print(total_sum(m, n, s))
