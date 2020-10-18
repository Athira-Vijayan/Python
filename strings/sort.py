str=[]
n=int(input('Enter the number of strings:'))

for i in range(n):
    print('enter string:',end='')
    str.append(input())
str.sort()
str1=sorted(str)

for i in str1:
    print(i)
