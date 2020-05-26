"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""
def fibonacci(n):
    """Поиск числа фибоначчи.
    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """
    fib1 = 1
    fib2 = 1
    number_in_order = int(input("Enter order number of Fibonatchi: "))
    i = 0
    while i < number_in_order - 2: # необходимое условие, т.к. первые два числа = 1
        fib_sum = fib1 + fib2 
        fib1 = fib2
        fib2 = fib_sum # присваиваем ф2 предыдущую сумму 
        i = 1 + i 
     return ("Your result is: " + str(fib2))
if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 0
    print(fibonacci(n))
