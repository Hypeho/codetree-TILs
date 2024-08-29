a,b,c = map(int, input().split())

if a <= (a and b and c):
    print(1,end=' ')
else:
    print(0,end=' ')

if a==b==c:
    print(1,end=' ')
else:
    print(0,end=' ')