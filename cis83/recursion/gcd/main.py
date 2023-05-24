"""
Determine the greatest common divisor
of two numbers, e.g., GCD(8, 12) = 4
"""


def gcd(n1, n2):
    if n1 == n2:   # Base case          
        return n1
    elif n1 < n2:  # Recursive case
      print('less than',n1,n2)
      return gcd(n1, n2 - n1)
    else:
      print('greater than',n1,n2)
      return gcd(n1 - n2, n2)

print ('This program outputs the greatest '
       'common divisor of two numbers.\n')

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if (num1 < 1) or (num2 < 1):
    print('Note: Neither value can be below 1.')
else:
    my_gcd = gcd(num1, num2)
    print(f'Greatest common divisor = {my_gcd}')