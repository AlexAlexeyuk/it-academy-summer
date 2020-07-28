def dct_():

    """ returns set """

    print({el: el ** 3 for el in range(1, 21)})


def counter_():

    """returns amount of 0  at the end of number"""

    i = 0
    num = int(input('enter an integer: '))
    if num:
        while not num % 10:
            num = num // 10
            i += 1
        print("The number at the end has " + str(i) + ' zeros')
    if not num:
        print('The number at the end has 1 zero')
