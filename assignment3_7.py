# program to print the pattern Qnor15
import re

f_open = open('xyz.txt')
for s in f_open:
    pat = re.findall(r'^F..m', s)
    if pat:
        print(pat)