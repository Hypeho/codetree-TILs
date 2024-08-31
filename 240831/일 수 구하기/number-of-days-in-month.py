n = int(input())

'''
if 1<=n<=7:
    if n%2==1:
        print(31)
    elif n==2:
        print(28)
    else:
        print(30)
else:
    if n%2==0:
        print(31)
    else:
        print(30)
'''

if n in (1,3,5,7,8,10,12):
    print(31)
elif n==2:
    print(28)
else:
    print(30)