def myarguments(name, lastname, age, favcolor='Blue'):

    print("\nHi ", name )
    print("\n ", lastname )
    print("\n  ", age )
    print("\n   ", favcolor )

# keyword arguments makes is so much more readable
myarguments(favcolor="Blue", age=69, lastname='Maldonado', name='Ray')

myarguments(age=69, lastname='Maldonado', name='Ray')