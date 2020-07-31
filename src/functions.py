""" returns.

set
"""


def dct_():
    print({el: el ** 3 for el in range(1, 21)})


"""returns amount of 0.

at the end of number
"""


def counter_():
    i = 0
    num = int(input('enter an integer: '))
    if num:
        while not num % 10:
            num = num // 10
            i += 1
        print("The number at the end has " + str(i) + ' zeros')
    if not num:
        print('The number at the end has 1 zero')
