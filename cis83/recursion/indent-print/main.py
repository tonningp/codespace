def find(lst, item, low, high, indent):
    """
    Finds index of string in list of strings, else -1.
    Searches only the index range low to high
    Note: Upper/Lower case characters matter
    """
    print(f'{indent} find() range {low} {high}')
    range_size = (high - low) + 1
    mid = (high + low) // 2

    if item == lst[mid]:  # Base case 1: Found at mid
        print(f'{indent} Found person.')
        pos = mid
    elif range_size == 1:  # Base case 2: Not found
        print(f'{indent} Person not found.')
        pos = -1
    else:  # Recursive search: Search lower or upper half
        if item < lst[mid]:  # Search lower half
            print(f'{indent} Searching lower half.')
            pos = find(lst, item, low, mid, indent + '   ')
        else:  # Search upper half
            print(f'{indent} Searching upper half.')
            pos = find(lst, item, mid+1, high, indent + '   ')

    print(f'{indent} Returning pos = {pos}.')
    return pos

attendees = []

attendees.append('Adams, Mary')
attendees.append('Carver, Michael')
attendees.append('Domer, Hugo')
attendees.append('Fredericks, Carlo')
attendees.append('Li, Jie')

name = input("Enter person's name: Last, First: ")
pos = find(attendees, name, 0, len(attendees)-1, '   ')

if pos >= 0:
    print(f'Found at position {pos}.')
else:
    print( 'Not found.')