print('Opening file alice.txt.')
with open('report.txt','w') as report:
    print('Reading file alice.txt.')
    with open('alice.txt','r') as f:
        for line in f:
            line = line.rstrip()
            if 'rabbit' in line.lower():
                report.write(f'{line}\n')
