n = 0
for i in range(1067, 3628):
    if i%2==0 and i%7==0:
        n += 1
        print(i)
print(n)
