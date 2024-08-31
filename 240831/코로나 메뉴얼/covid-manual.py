a = input().split()
cold1, tem1 = str(a[0]), int(a[1])

b = input().split()
cold2, tem2 = str(b[0]), int(b[1])

c = input().split()
cold3, tem3 = str(c[0]), int(c[1])

# 첫 번째 조건
if cold1 == 'Y' and tem1 >= 37:
    d = 'A'
elif cold1 == 'N' and tem1 >= 37:
    d = 'B'
elif cold1 == 'Y' and tem1 < 37:
    d = 'C'
else:
    d = 'D'

# 두 번째 조건
if cold2 == 'Y' and tem2 >= 37:
    e = 'A'
elif cold2 == 'N' and tem2 >= 37:
    e = 'B'
elif cold2 == 'Y' and tem2 < 37:
    e = 'C'
else:
    e = 'D'

# 세 번째 조건
if cold3 == 'Y' and tem3 >= 37:
    f = 'A'
elif cold3 == 'N' and tem3 >= 37:
    f = 'B'
elif cold3 == 'Y' and tem3 < 37:
    f = 'C'
else:
    f = 'D'

# 결과 확인
if d == 'A' and e == 'A' and f == 'A':
    print('E')
elif d == 'A' and e == 'A':
    print('E')
elif d == 'A' and f == 'A':
    print('E')
elif e == 'A' and f == 'A':
    print('E')
else:
    print('N')