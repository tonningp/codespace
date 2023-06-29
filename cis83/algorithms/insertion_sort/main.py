import random

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        j = i
        # Insert numbers[i] into sorted part 
        # stopping once numbers[i] in correct position
        while j > 0 and numbers[j] < numbers[j - 1]:
            # Swap numbers[j] and numbers[j - 1]
            temp = numbers[j]
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = temp
        print(numbers)

# Driver code to test above
random.seed("ABC")
numbers = [random.randint(0,10000) for _ in range(100000)]
print('UNSORTED:', end=' ')
for num in numbers:
    print(num, end=' ')
print()
 
insertion_sort(numbers)
print('SORTED:', end=' ')
for num in numbers:
    print(num, end=' ')
print()
