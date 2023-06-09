my_list1 = ["Mexico", "Portugal", "USA", "Ecuador", "El Salvador", "Republica Dominicana", "Peru"]
my_list2 = ["Haiti", "Venezuela", "Guatemala"]

print(len(my_list1))
print(my_list1[0:2])

print(my_list1)
print(my_list1[2:6])

# slice all but the last one
print(my_list1[0:-1])

# add one value
my_list1.append("Canada")
print(my_list1)

# adding to the middle of the list
my_list1.insert(3, "Camerun")
print(my_list1)

# Get index
print(my_list1.index("Canada"))

# Remove last item from the list
my_list1.pop()
print(my_list1)

# Sort
my_list1.sort()
print(my_list1)

# Reverse Sorting
my_list1.sort(reverse=True)
print(my_list1)

# Adding 2 lists
list3 = my_list1 + my_list2
print(list3)

# Clearing List
# list3.clear()
# del list3

list4 = list3.copy()
print(list4)