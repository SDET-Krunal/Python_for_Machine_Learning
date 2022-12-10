import numpy as np

n1 = np.array([1, 2, 3, 4, 5])
n2 = np.array([2, 4, 6, 8, 10])


# NumPy Array Intersection and Difference functions:
# ===================================================

# 1. intersect1d() - Returns array of common numbers available in given two arrays.
# ----------------------------------------------------------------------------------

print("Intersection of two arrays {} and {} :: {}".format(n1, n2, np.intersect1d(n1, n2)))
# O/p => Intersection of two arrays [1 2 3 4 5] and [ 2  4  6  8 10] :: [2 4]


# 2. setdiff1d() - Returns array of numbers by excluding the numbers presents in another array.
# ----------------------------------------------------------------------------------------------

print("Difference of {} array :: {}".format(n1, np.setdiff1d(n1, n2)))
# O/p => Difference of [1 2 3 4 5] array :: [1 3 5]
# Explanation: Here, It excludes 2 and 4 from array n1 because they're present in another array n2

print("Difference of {} array :: {}".format(n2, np.setdiff1d(n2, n1)))
# O/p => Difference of [ 2  4  6  8 10] array :: [ 6  8 10]
# Explanation: Here, It excludes 2 and 4 from array n2 because they're present in another array n1
