'''Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,

 кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
 одновременно кратных и 3 и 5 - FizzBuzz'''

enter = int(input('Enter any number: '))
while enter < 100:
  if not enter % 3 and enter % 5:
    print('FizzBuzz')
  elif not enter % 5:
    print('Buzz')
  elif not enter % 3:
    print ('Fizz')
  else:
    print(enter)
  enter += 1
