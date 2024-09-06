n = int(input())
a,b,c = 0,0,0

for i in range(1,n+1):
    if i % 2 == 0:
        if i % 12 == 0:
            c += 1
        elif i % 3 == 0:
            b += 1
        else:
            a += 1
    elif i % 3 == 0:
        b += 1
print(a,b,c)