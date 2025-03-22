numbers = [2, 5, 3, 1, 6, 4]
#To add at end
numbers.append(20)
print(numbers)

#TO insert numbers at specific position
numbers.insert(0, 10)
print(numbers)

#To remove the first occurrence of a value
numbers.remove(5)
print(numbers)

#To remove the list
numbers.clear()
print(numbers)

#To remove the last element
numbers = [2, 5, 3, 1, 6, 5, 4]
numbers.pop()
print(numbers)

#To get the index of specific number
print(numbers.index(5))

print(50 in numbers)

#To count the number of occurrences of a value
print(numbers.count(5))

#To sort the list in ascending order
numbers.sort()
print(numbers)

#TO reverse the list
numbers.reverse()
print(numbers)

#To copy the list
numbers2 = numbers.copy()
numbers.append(20)
print(numbers2)