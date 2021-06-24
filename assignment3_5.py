# program to find the pattern Qno11
import re
# name = open(input('Enter the file name:'))
# s = name.read()
s = "cghdghdgchd from@65: shydu67676yhfudyfudyfudy"
x = re.findall(r'from.[0-9][0-9]:', s)
c = str(x)
a = re.findall('\d{2}',c)
print(x)
if a > ['0']:
    print(a)
else:
    print('number is zero')
