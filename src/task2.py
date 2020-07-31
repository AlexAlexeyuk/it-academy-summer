"""Дан список стран и городов каждой страны.

Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
"""

result = {}
for i in range(int(input("How many conties and city: "))):
    country, *cities = input("Enter contry and cities: ").split()
    for city in cities:
        result[city] = country

for i in range(int(input("How many cities will you enter: "))):
    print(result[input("enter city: ")])
