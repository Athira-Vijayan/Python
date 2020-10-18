#python program to find sum of even numbers using command line arguments
import sys
args=sys.argv[1:]
print(args)
sum=0
for a in args:
    x=int(a)
    if(x%2==0):
        sum+=x
print('sum=',sum)
