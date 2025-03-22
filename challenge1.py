number = [5, 2, 5, 2, 2]

for x in number:
    print('x'*x)

print("\nAnother way")

#another way
for x_count in number:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)