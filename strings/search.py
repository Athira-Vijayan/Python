#searching for a sstring in a group of strings
str=[]
n=int(input('How many strings?'))
for i in range(n):
     print('enetr string:',end='')
     str.append(input())
s=input('Enter the key to search:')
flag=False
for i in range(len(str)):
    if s==str[i]:
        flag=True
        print('Found at',i+1)
else:
    print('Not found')
#if flag==False:
#    print('Not found')
