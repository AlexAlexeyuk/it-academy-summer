def longest_word(str_):

    """Поиск самого длинного слова в предложении.
    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
    несколько, самое левое в строке).
    в случае если
    """

    str_ = input("Enter some words: ")
    return("the longest word is: " + max(str_.strip("!#$%&'()*+, -./:;<=>?@[\]^_`{|}~'").split(), key = len))
if __name__ == '__main__':
    str_ = ''
    print(longest_word(str_))
