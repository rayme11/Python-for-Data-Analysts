# Similar to lists but once they are immutable
# Once created they can't be changed
# can't add or remove items once created
# Uses parentheses instead of square brackets as in the list

simple_tuple = ("Value 1", "Value 2", "Value 3", "Value 4")
print(type(simple_tuple))

print(simple_tuple[0])

# Converting to Tuple
my_name_is = "Raymundo"
my_name_as_a_tuple = tuple(my_name_is)
print(my_name_as_a_tuple)