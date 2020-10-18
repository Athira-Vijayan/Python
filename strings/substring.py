#to find first occurrence od sub string in a main string
str=input('enter string:')
sub=input('enter sub string:')
try:
    n=str.index(sub,0,len(str)) #in find method, str.find(sub,0,len(str))
except ValueError:
    print('Sub string not found')

else:
    print('string found at:',n+1)
