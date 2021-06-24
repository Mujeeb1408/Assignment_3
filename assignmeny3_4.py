# program to validate the password Qnor10
import re
n = str(input('Enter the password with max 6 characters:'))
x = True
while x:
    if len(n) > 6:
        break
    elif not re.search('[a-zA-Z]', n):
        break
    elif not re.search('[0-9]', n):
        break
    elif not re.search('..', n):
        break
    elif re.search('\s', n):
        break
    else:
        print('Valid password')
        x = False
        break
if x:
    print('Not a valid password')