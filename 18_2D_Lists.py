matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])
matrix[0][1] = 20
print(matrix[0][1])

#Using nested loop
print("\nUsing nested loops")
for row in matrix:
    for items in row:
        print(items)