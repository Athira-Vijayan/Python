n=int(input('enter lowest:'))
m=int(input('enter highest:'))
for i in range(n,m+1):
    for j in range(n
    ,i):
        if(i%j)==0:
            break
    else:
        print(i)
