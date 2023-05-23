print('Opening file pg2600.txt.')
with open('pg2600.txt','r') as f:
    #f = open('pg2600.txt')  # create file object
    print('Reading file pg2600.txt.')
    warcount = 0
    peacecount = 0
    for line in f:
        line = line.rstrip()
        lowerLine = line.lower()
        if any([' war ' in lowerLine,
                'war,' in lowerLine,
                'war.' in lowerLine,
                'war;' in lowerLine,
                ]
               ):
            warcount += 1
        if ' peace ' in lowerLine:
            peacecount += 1
        #print(line)
    print('war appears',warcount,'times')
    print('peace appears',peacecount,'times')
    print('ratio of war to peace',warcount/peacecount,'to 1')
    #contents = f.read()  # read file text into a string
    #print('\nContents of pg2600.txt:')
    #print(contents)
