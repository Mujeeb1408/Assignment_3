# program to store the numbers in list and printing sum avg
ipNors = []
sum = 0
n = int(input('Enter the number of elements:'))
for num in range(0,n):
    num = int(input())
    sum = sum+num
    ipNors.append(num)
print('The given numbers are: ', ipNors)
print('Sum of the entered numbers is:', sum)
print('Average od the entered numbers is: ',(sum/n))