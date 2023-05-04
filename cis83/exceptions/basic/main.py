def prompt_for_integer(prompt):
    count=0
    while count < 3:
        try:
            count += 1
            ret = int(input(prompt))
            return ret
        except ValueError:
            print('Invalid integer, try again')
    raise ValueError('Three times you got it wrong')
            
try:
    i = prompt_for_integer("Enter a value to divide into 42: ")
    print(42 // i)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)