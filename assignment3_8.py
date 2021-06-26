# program to find pattern Qnor16
import re

lst = []
lst1 = []
sum = 0
s = open('prgrm8.txt', 'r')
for a in s:
    pat = re.findall(r'^X\S:\d*', a)
    s1 = str(pat)
    nums = re.findall('\d+', s1)
    lst.append(nums)
    print(pat)
for i in range(0, len(lst)):
    lst1 = lst1 + lst[i]
    lst1[i] = int(lst1[i])
    sum = sum + lst1[i]
# print(lst1)
print('Sum of numbers present after colon is :',(sum))


