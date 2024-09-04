a = input().split()
c = str(a[0])
n = int(a[1])

if c=='A':
    for i in range(1,n+1):
        print(i,end=' ')
else:
    for j in range(n,0,-1):
        print(j,end=' ')