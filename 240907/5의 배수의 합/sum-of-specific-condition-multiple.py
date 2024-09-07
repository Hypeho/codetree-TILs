a,b = map(int, input().split())
s = 0

if a<=b+1:
    for i in range(a,b+1):
        if i % 5 == 0:
            s += i
else:
    for i in range(b,a+1):
        if i % 5 == 0:
            s += i

print(s)