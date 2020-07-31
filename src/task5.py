"""Каждый из N школьников некоторой школы знает Mi языков.

 Определите, какие языки знают все школьники и языки,
 которые знает хотя бы один из школьников.
 """

students = [{input() for j in range(int(input()))}
            for i in range(int(input()))]
known_by_everyone = set.intersection(*students)
known_by_someone = set.union(*students)
print(len(known_by_everyone))
print(known_by_everyone)
print(len(known_by_someone))
print(known_by_someone)
