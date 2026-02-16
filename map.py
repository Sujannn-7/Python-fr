l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

square = lambda n: n*n

sqlist = map(square, l)
print(list(sqlist))