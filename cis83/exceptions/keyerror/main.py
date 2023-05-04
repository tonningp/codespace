fruit = {'apples':10,'oranges':10}
try:
    f = input("Enter fruit key: ")
    for i in range(3):
        print(f'{i} {fruit[f]}')
except KeyError as ke:
    print("The key was invalid, program is ending now.")