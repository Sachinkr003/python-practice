# List comprehension = A cocise way to create lists in python
#                      compact and easier to read then traditional loops
#                      [expression for value in itreable if condition]

doubles = []
for x in range(1, 14):
    doubles.append(x * 2)

print(doubles)