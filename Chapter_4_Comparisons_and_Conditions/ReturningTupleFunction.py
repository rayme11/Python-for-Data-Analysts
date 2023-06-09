def square_and_cub(num):
    square = num ** 2
    cube = num ** 3

    return square,cube

square, cube = square_and_cub(9)
print(type(square_and_cub(9)))
print(square_and_cub(3))
