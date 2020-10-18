list = [23,5,78,90,100,145]
key = int(input('enter the number to be found:'))
for i in list:
    if key == i:
        print('found')
        break
else:
    print('not found')
