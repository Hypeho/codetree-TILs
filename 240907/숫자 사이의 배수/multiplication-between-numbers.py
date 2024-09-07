a,b = map(int, input().split())
s = 0
c = 0

for i in range(a,b+1):
    if i % 5 == 0 or i % 7 == 0:
        s += i
        c += 1

print(f'{s} {s/c:.1f}')