num = [1,2,3,4,5]
smallest=None
for value in num:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value

print('Smallest number is',smallest)
