# List comprehension = A cocise way to create lists in python
#                      compact and easier to read then traditional loops
#                      [expression for value in itreable if condition]

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10, 23, 24]

positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(odd_nums)