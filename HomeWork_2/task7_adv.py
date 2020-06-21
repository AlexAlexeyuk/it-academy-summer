'''If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples
of 3 or 5 below the number passed in.Note: If the number is
a multiple of both 3 and 5, only count it once.'''
number = 14

i = 3
j = 5
n_tree = 0
n_five = 0
while i < number:
    n_tree = n_tree + i
    i += 3
while j < number:
    n_five = n_five + j
    j += 5
print(n_five + n_tree)
