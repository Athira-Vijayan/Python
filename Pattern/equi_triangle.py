n=int(input('enter the number of rows:'))
for i in range(1,n+1):
    print(' '*(n-i)+'* '*(i)) #another simpler approach
    #print(' '*n,end='')
    #print('* '*i)
    #n-=1
