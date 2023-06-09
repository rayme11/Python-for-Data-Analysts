for char in "Raymundo":
    print(char)

# this will throw error as it is not iterable
# for integer in 989898989:
#     print(integer)

myTuple=('a','b','c')
print(type(myTuple))

for c in myTuple:
    print(c)

# converting range to tuple or list
r = range(10)
print(r)

range_to_list = list(r)
print('\nRange to list ' + str(range_to_list))

range_to_tuple = tuple(r)
print('\nRange to tuple ' + str(range_to_tuple))

# range - print from to 9, excluding 10
# range only accepts integer values
for i in range(2,10):
    print(i)

# skipping in range
for i in range(2,20,2):
    print(i)

# Condition

car = input('\nWhat is your favorite car ')
while car.upper() != 'BMW':
    car = input('\nTry again, wrong brand ')

print('Got a good car')