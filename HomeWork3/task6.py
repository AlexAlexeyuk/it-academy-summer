"""Дан список целых чисел.

Требуется переместить все ненулевые элементы в левую часть списка, не меняя их порядок,
а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя, дополнительный список использовать
нельзя, задачу нужно выполнить за один проход по списку. Распечатайте полученный список.
"""

list_ = [1, 4, 2, 0, 4, 5, 0]
print([i for i in list_ if i] + [0]*list_.count(0)) 
