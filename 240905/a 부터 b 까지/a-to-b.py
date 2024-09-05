a,b = map(int, input().split())

print(a, end=' ')

for i in range(a,b+1):
    if i % 2 == 0 and i <=b :
        i += 3
        print(i)
    elif i % 2 != 0 and i <= b:
        i *= 2