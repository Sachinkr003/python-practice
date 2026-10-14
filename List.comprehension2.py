# List comprehension = A cocise way to create lists in python
#                      compact and easier to read then traditional loops
#                      [expression for value in itreable if condition]

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(squares)