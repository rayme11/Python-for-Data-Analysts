salary = 10000
expenses = 770
print('First Example-----------')
living_within_means = False

if salary - expenses > 0:
    living_within_means =  True
    print("I am living within means?", str(living_within_means) + '\n')
else:
    print("not living within means\n")


print('Second Example-----------')
classic_cars = ["Pierce Arrow", "Oldsmobile", "Mustang", "Porsche 911"]

car = 'Ferrari'

if car in classic_cars:
    print('You car is within the class cars:' , car)