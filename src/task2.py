"""Создайте декоратор, который хранит результаты вызова функции.

(за все время вызовов, не только текущий запуск программы)
"""


def dec_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('result.txt', 'a') as f:
            f.write(result)
        return result
    return wrapper


@dec_result
def count(a, b):
    return a + b


print(count("a", "b"))
print(count("c", "d"))
