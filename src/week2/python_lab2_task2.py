"""
Lab 3.2 – Comprehensions and Transformations

Goals:
- Practice list, set, and dictionary comprehensions.
- Transform and filter data concisely.

Instructions:
Given the list:
    numbers = [3, 8, -2, 7, 0, -5, 10]

1. Create a list `squares` with the square of each number.
2. Create a list `positives` containing only positive numbers.
3. Create a set `even_squares` of the squares of even numbers.
4. Create a dictionary `cubes` mapping each number to its cube.
5. Print all results.
"""

# Given list of numbers
numbers = [3, 8, -2, 7, 0, -5, 10]

# 1. List of squares
squares = [x**2 for x in numbers]

# 2. List of positive numbers
positives = [x for x in numbers if x > 0]

# 3. Set of even number squares
even_squares = {x**2 for x in numbers if x % 2 == 0}

# 4. Dictionary mapping numbers to their cubes
cubes = {x: x**3 for x in numbers}

# 5. Print results
print("Numbers:", numbers)
print("Squares:", squares)
print("Positives:", positives)
print("Even squares:", even_squares)
print("Cubes:", cubes)
