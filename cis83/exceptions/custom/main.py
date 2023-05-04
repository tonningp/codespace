class LessThanZeroError(Exception):
    def __init__(self, value):
        self.value = value

my_num = int(input('Enter number: '))

if my_num < 0:
    raise LessThanZeroError('my_num must be greater than 0')
else:
    print(f'my_num: {my_num}')