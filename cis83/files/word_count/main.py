print('Opening file alice.txt.')
with open('alice.txt','r') as f:
    #f = open('pg2600.txt')  # create file object
    print('Reading file alice.txt.')
    warcount = 0
    peacecount = 0
    for line in f.readlines():
        line = line.rstrip()
        if 'war' in line.lower():
            print(line)
            warcount += 1
        if 'peace' in line.lower():
            peacecount += 1
        #print(line)
    print('war appears',warcount,'times')
    print('peace appears',peacecount,'times')
    if peacecount > 0:
        print('ratio of war to peace',warcount/peacecount,'to 1')
    #contents = f.read()  # read file text into a string
    #print('\nContents of pg2600.txt:')
    #print(contents)
