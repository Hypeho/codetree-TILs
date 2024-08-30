a = input().split()
age1, gen1 = int(a[0]), str(a[1])

b = input().split()
age2, gen2 = int(b[0]), str(b[1])

if (age1>=19 and gen1=='M') or (age2>=19 and gen2=='M'):
    print(1)
else:
    print(0)