#inverted number pyramid in descending order
n=int(input('enter number of rows:'))
b=n+1
for i in range(n,0,-1):
    b-=1
    for j in range(1,i+1):
        print(b,end='')
    print()
#4444
#333
#22
#1
