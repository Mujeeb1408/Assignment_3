# program that accepts strings and returns the number of letters,digits,uppercase,
# lower case in dictionary
import re

Dic = {}
string = str(input('Enter a string:'))
Letters=re.findall('[a-z]|[A-Z]',string)
UpperCase = re.findall('[A-Z]', string)
LowerCase = re.findall('[a-z]', string)
Digits = re.findall('[0-9]', string)
Dic['Letters'] = len(Letters)
Dic['UpperCase'] = len(UpperCase)
Dic['LowerCase'] = len(LowerCase)
Dic['Digits'] = len(Digits)
print(Dic)
