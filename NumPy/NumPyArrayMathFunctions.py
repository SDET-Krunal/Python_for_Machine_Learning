import numpy as np

n1 = np.array([1, 2, 3, 4, 5])
n2 = np.array([6, 7, 8, 9, 10])


# NumPy Array Mathematics functions:
# ===================================================

print("Sum of all numbers from both arrays :: {}".format(np.sum([n1, n2])))
# O/p => Sum of all numbers from both arrays :: 55

print("Sum of numbers that are present at index 0 :: {}".format(np.sum([n1, n2], axis=0)))
# O/p => Sum of numbers that are present at index 0 :: [ 7  9 11 13 15]

print("Sum of numbers that are present at index 1 :: {}".format(np.sum([n1, n2], axis=1)))
# O/p => Sum of numbers that are present at index 1 :: [15 40]
