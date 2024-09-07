s,c = 0,0

for i in range(10):
    n = int(input())
    if 0<=n<=200:
        s += n
        c += 1

print(f'{s} {s/c:.1f}')