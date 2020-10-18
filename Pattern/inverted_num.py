n=int(input('enter the number of rows:'))
x=0
for i in range(n,0,-1):
    x+=1
    for j in range(1,i+1):
        print(x,end='')
    print()
#1111
#222
#33
#4
