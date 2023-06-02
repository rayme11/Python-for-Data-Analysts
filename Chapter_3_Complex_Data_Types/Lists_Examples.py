int_list = [1, 3, 5, 7, 9, 10]

for item in int_list:
    print(item)

if 3 in int_list:
    print('Item was found')

print('List has # of items', len(int_list), sep = ':')

# Update item in list
int_list[3] = 100

print(int_list)