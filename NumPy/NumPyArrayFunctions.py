import numpy
import numpy as np

# Single-dimensional Array
sda = np.array([1, 2, 3, 4, 5])
print("Single-dimensional Array :: {}".format(sda))
# O/p => Single-dimensional Array :: [1 2 3 4 5]


# Multi-dimensional Array
mda = np.array(([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
print("Multi-dimensional Array :: {}".format(mda))
# O/p => Multi-dimensional Array :: [[ 1  3  5  7  9]
#                                    [ 2  4  6  8 10]]


# NumPy Array functions:
# =======================

# 1. zeros() - Initialize NumPy arrays with zero only.
# -----------------------------------------------------

za = np.zeros((2, 3), dtype=numpy.int8)
print("Zero's array :: {}".format(za))
# O/p => Zero's array :: [[0 0 0]
#                         [0 0 0]]


# 2. full() - Initialize NumPy arrays with given particular number only.
# -----------------------------------------------------------------------

fa = np.full((3, 5), 4)
print("Array with given number :: {}".format(fa))
# O/p => Array with given number :: [[4 4 4 4 4]
#                                    [4 4 4 4 4]
#                                    [4 4 4 4 4]]


# 3. arange() - Initialize NumPy arrays with given particular range.
# -------------------------------------------------------------------

ara1 = np.arange(1, 6)
print("arange array 1 :: {}".format(ara1))
# O/p => arange array 1 :: [1 2 3 4 5]

ara2 = np.arange(1, 50, 3)
print("arange array from range 1 to 50 with difference 3 :: {}".format(ara2))
# O/p => arange array from range 1 to 50 with difference 3 :: [ 1  4  7 10 13 16 19 22 25 28 31 34 37 40 43 46 49]


# 4. random.randint() - Initialize NumPy arrays with random numbers.
# -------------------------------------------------------------------

rra = np.random.randint(1, 50, 7)
print("Random array numbers between 1 to 50 :: {}".format(rra))
# O/p => Random array numbers between 1 to 50 :: [40 31 47 45 17 18 23]


# 5. shape() - returns shape of given array.
#    e.g: (2, 3) - 2 rows and 3 columns
# -------------------------------------------------------------------

sda1 = np.array([[1, 3, 5]])
print("Shape of given array :: {}".format(sda1.shape))
# O/p => Shape of given array :: (1, 3)

mda1 = np.array([[1, 3, 5], [2, 4, 6]])
print("Shape of given array :: {}".format(mda1.shape))
# O/p => Shape of given array :: (2, 3)
