# program to find pattern Qnor16
import re

s = open('prgrm8.txt', 'r')
for a in s:
    pat = re.findall(r'^X\S:\d*', a)
    s1 = str(pat)
    nums = re.findall('\d+',s1)
    print(pat)

