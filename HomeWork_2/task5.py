def fibonacci(n):

    """Поиск числа фибоначчи.
    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи"""

    n = int(input("enter number in order fibonacci: "))
    fib1 = fib2 = 1
    for element in range(3, n + 1):
      fib1, fib2 = fib2, fib1 + fib2
    return fib2

if __name__ == '__main__':
    n = 0
    print(fibonacci(n))
