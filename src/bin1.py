def square_degree_counter(number):
    """Написать программу которая находит ближайшую
    степень двойки к введенному числу.
    10(8), 20(16), 1(1)
    """
    dgr = 0
    while True:
        res1 = abs(number - (1 << dgr))
        res2 = abs(number - (1 << dgr + 1))
        if res2 > res1:
            break
        else:
            dgr += 1
    return '{}'.format(1 << dgr)

print(square_degree_counter(10))
print(square_degree_counter(20))


