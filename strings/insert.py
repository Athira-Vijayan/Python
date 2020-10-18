#insert a substring in the given index of a string
s1=input('enter the first string:')
s2=input('enter the second string:')
n=int(input('enter the index:'))
res=s1[:n]+' '+s2+' '+s1[n:]
print(res)
