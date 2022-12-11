import numpy as np

n1 = np.array([1, 2, 3, 4, 5])
n2 = np.array([6, 7, 8, 9, 10])


# NumPy Array Mathematics functions:
# ===================================

# 1. sum() - Returns sum of all number available in NumPy arrays.
# ----------------------------------------------------------------

print("Sum of all numbers from both NumPy arrays {} and {} :: {}".format(n1, n2, np.sum([n1, n2])))
# O/p => Sum of all numbers from both NumPy arrays [1 2 3 4 5] and [ 6  7  8  9 10] :: 55

print("Sum of numbers that are present at index 0 :: {}".format(np.sum([n1, n2], axis=0)))
# O/p => Sum of numbers that are present at index 0 :: [ 7  9 11 13 15]

print("Sum of numbers that are present at index 1 :: {}".format(np.sum([n1, n2], axis=1)))
# O/p => Sum of numbers that are present at index 1 :: [15 40]


# 2. Basic Addition - Adds given number into all number available in NumPy arrays.
# ---------------------------------------------------------------------------------

print("NumPy array {} after the addition of number {} :: {}".format(n1, 2, n1+2))
# O/p => NumPy array [1 2 3 4 5] after the addition of number 2 :: [3 4 5 6 7]

print("NumPy array {} after the addition of number {} :: {}".format(n2, 5, n2+5))
# O/p => NumPy array [ 6  7  8  9 10] after the addition of number 5 :: [11 12 13 14 15]


# 3. Basic Subtraction - Subtracts given number from all number available in NumPy arrays.
# -----------------------------------------------------------------------------------------

print("NumPy array {} after the subtraction of number {} :: {}".format(n2, 3, n2-3))
# O/p => NumPy array [ 6  7  8  9 10] after the subtraction of number 3 :: [3 4 5 6 7]

print("NumPy array {} after the subtraction of number {} :: {}".format(n1, 1, n1-1))
# O/p => NumPy array [1 2 3 4 5] after the subtraction of number 1 :: [0 1 2 3 4]


# 4. Basic Multiplication - Multiplies given number with all number available in NumPy arrays.
# ---------------------------------------------------------------------------------------------

print("NumPy array {} after multiply by number {} :: {}".format(n2, 4, n2*4))
# O/p => NumPy array [ 6  7  8  9 10] after multiply by number 4 :: [24 28 32 36 40]

print("NumPy array {} after multiply by number {} :: {}".format(n1, 6, n1*6))
# O/p => NumPy array [1 2 3 4 5] after multiply by number 6 :: [ 6 12 18 24 30]


# 5. Basic Division - Divides given number from all number available in NumPy arrays.
# ------------------------------------------------------------------------------------

print("NumPy array {} after divided by number {} :: {}".format(n2, 4, n2/4))
# O/p => NumPy array [ 6  7  8  9 10] after divided by number 4 :: [1.5  1.75 2.   2.25 2.5 ]

print("NumPy array {} after divided by number {} :: {}".format(n2, 2, n2/2))
# O/p => NumPy array [ 6  7  8  9 10] after divided by number 2 :: [3.  3.5 4.  4.5 5. ]


# 6. Mean - Returns mean value of given NumPy arrays.
# ----------------------------------------------------
# Explanation: Mean value is obtained by dividing the sum of all values by total numbers.

print("Mean value of NumPy array {} :: {}".format(n1, np.mean(n1)))
# O/p => Mean value of NumPy array [1 2 3 4 5] :: 3.0

print("Mean value of NumPy array {} :: {}".format(n2, np.mean(n2)))
# O/p => Mean value of NumPy array [ 6  7  8  9 10] :: 8.0


# 7. Median - Returns mean value of given NumPy arrays.
# ------------------------------------------------------
# Explanation: Mean value is obtained by dividing the sum of all values by total numbers.

print("Median value of NumPy array {} :: {}".format(n1, np.median(n1)))
# O/p => Median value of NumPy array [1 2 3 4 5] :: 3.0

print("Median value of NumPy array {} :: {}".format(n2, np.median(n2)))
# O/p => Median value of NumPy array [ 6  7  8  9 10] :: 8.0


# 8. Standard deviation - Returns mean value of given NumPy arrays.
# ------------------------------------------------------------------

print("Standard deviation of NumPy array {} :: {}".format(n1, np.std(n1)))
# O/p => Standard deviation of NumPy array [1 2 3 4 5] :: 1.4142135623730951

print("Standard deviation of NumPy array {} :: {}".format(n2, np.std(n2)))
# O/p => Standard deviation of NumPy array [ 6  7  8  9 10] :: 1.4142135623730951
