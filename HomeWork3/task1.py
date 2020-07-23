"""FIZZBUZZ.

Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
 кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
 одновременно кратных и 3 и 5 - FizzBuzz
"""

enter = int(input('Enter one: '))
while enter < 100:
  print("Fizz" * (not enter % 3 ) + "Buzz" * (not enter % 5 ) or enter)
  enter += 1
