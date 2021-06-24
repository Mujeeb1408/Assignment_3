# Program to accept nors and printing sum of even and product of odd numbers Qnor13

n = int(input('Enter the number of elements:'))
lst = []
evenlst=[]
oddlst=[]
i = 0
sum = 0
product = 1
print('Enter the numbers')
while i < n:
    a = int(input())
    lst.append(a)
    i = i + 1
    if a % 2 == 0:
        evenlst.append(a)
        sum = sum+a
    else:
        oddlst.append(a)
        product = product*a
print('Entered numbers are: ',lst)
print('Even numbers: ',evenlst)
print('Sum of even Numbers is: ',sum)
print('Odd number:',oddlst)
print('Product of odd Numbers is: ',product)