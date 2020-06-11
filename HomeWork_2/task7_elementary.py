import re
'''Need to print amout of 
zeros at the end of the integer'''
i=0
num = int(input('enter an integer: '))
if num:
    while not num % 10:
            num = num//10;
            i +=1 
    print ("The number at the end has " + str(i) + ' zeros')
if not num:
    print('The number at the end has 1 zero')
#prints a tuple with 3 elements - first, third and second to the last
elements = tuple(input("Enter number after coma: "))
print(tuple(elements[i] for i in [0,2,-2]))
#prints the first word in a given text.
pattern=r"[a-zA-Z']+"
text = input("Enter a text: ")
match=re.findall(pattern, text)
print(text.split()[0])
