x = range(3, 100, 2)
for i in x:
    print(i)
    if i == 51:
        break

print('*********')
# skipping current iteration with continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print('*********')
# skipping current iteration with pass
for i in range(5, 31):
    if 10 <= i <= 20:
        pass
    else:
        print(i)
