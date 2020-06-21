def palindrom(n):
    
"""Поиск числа фибоначчи.
:param n: Число.
:return: Bool. True или False. 
Является ли число палиндромом."""

    n = k = int(input("Enter any integer: "))
    n2 = 0
    while n > 0:
        left = n % 10; 
        n = n // 10; 
        n2 = n2 * 10 ;
        n2 = n2 + left;
    if n2 == k:
        return True
    else:
        return False

if __name__ == '__main__':
    n = 0
    print(palindrom(n))
