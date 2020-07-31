"""В файле хранятся данные с сайта IMDB.

Скопированные данные хранятся в файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt –
названия файлов, ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""

lst_top250 = []
ratings = {}
years = {}

try:
    with open('ratings.list', 'r') as full_f:
        for line in full_f:
            if 'Distribution' in line:
                break
        line = full_f.readline()
        while line != '\n':
            lst_top250.append(line)
            line = full_f.readline()

    for film in lst_top250:
        data = film.split()
        if data[2] not in ratings:
            ratings[data[2]] = '+'
        else:
            ratings[data[2]] += '+'
        if data[-1] not in years:
            years[data[-1]] = '+'
        else:
            years[data[-1]] += '+'
        title = ' '.join(data[3:-1]) + '\n'
        with open('top250_movies.txt', 'a+') as sub_f:
            sub_f.seek(0)
            if title not in sub_f:
                sub_f.write(title)

    with open('ratings.txt', 'w') as rat_f:
        for key in ratings:
            rat_f.write(key + ' ' + ratings[key] + '\n')
    with open('years.txt', 'w') as year_f:
        for key in sorted(years):
            year_f.write(key + ' ' + years[key] + '\n')

except FileNotFoundError:
    print('The file does not exist!')
