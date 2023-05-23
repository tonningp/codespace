import os

for dirname, subdirs, files in os.walk('.'):
    print(dirname, 'contains subdirectories:', subdirs, end=' ')
    print('and the files:', files)
