"""Вводится число найти его максимальный делитель.

являющийся степенью двойки. 10(2) 16(16), 12(4)
"""

def max_div(i):
    degree = 0
    div = 1
    while True:
        new_div = 1 << degree
        if not i % new_div:
            degree += 1
            div = new_div
        else:
            break
    return div
print(max_div(12))
