def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
    
        # Swap numbers[i] and numbers[index_smallest]
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp
        print(numbers)

            
numbers = [10, 2, 78, 4, 45,]
print('UNSORTED:', end=' ')
for num in numbers:
    print(num, end=' ')
print()

selection_sort(numbers)
print('SORTED:', end=' ')
for num in numbers:
    print(num, end=' ')
print()