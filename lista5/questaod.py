count = 0
a = range(18644, 33088)
for i in a:
    if 2 in i and 7 not in i:
        count += 1
print(count)
