n=int(input('enter the number of rows:'))
for i in range(n,0,-1):
    print(' '*(n-i),end='')
    print('* '*i)#remove the space we will get inverted right triangle
