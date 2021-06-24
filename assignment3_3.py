# program to read all lines in the file and printing email id's

import re
name=str(input('Enter the file name: '))
fopen = open(name)
f = fopen.read()
x = re.findall(r'[\w\.-]+@[\w\.-]+', f)
print('Mail ids are')
for a in x:
    print(a)