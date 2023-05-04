nums = []
rd_nums = -1
my_file = input('Enter file name: ')

try:
    print('Opening', my_file)
    rd_nums = open(my_file, 'r')  # Might cause IOError

    for line in rd_nums:
        nums.append(int(line))  # Might cause ValueError
except IOError:
    print(f'Could not find {my_file}')
except ValueError:
    print(f'Could not read number from {my_file}')
finally:
    print(f'Closing {my_file}')
    if rd_nums != -1:
        rd_nums.close()
    print(f'Numbers found: {" ".join([str(n) for n in nums])}')