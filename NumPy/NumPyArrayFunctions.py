import numpy
import numpy as np

# Single-dimensional Array
sda = np.array([1, 2, 3, 4, 5])
print("Single-dimensional NumPy Array :: {}".format(sda))
# O/p => Single-dimensional NumPy Array :: [1 2 3 4 5]


# Multi-dimensional Array
mda = np.array(([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
print("Multi-dimensional NumPy Array :: {}".format(mda))
# O/p => Multi-dimensional NumPy Array :: [[ 1  3  5  7  9]
#                                          [ 2  4  6  8 10]]


# NumPy Array functions:
# =======================

# 1. zeros() - Initialize NumPy arrays with zero only.
# -----------------------------------------------------

za = np.zeros((2, 3), dtype=numpy.int8)
print("Zero's NumPy array :: {}".format(za))
# O/p => Zero's NumPy array :: [[0 0 0]
#                               [0 0 0]]


# 2. full() - Initialize NumPy arrays with given particular number only.
# -----------------------------------------------------------------------

fa = np.full((3, 5), 4)
print("NumPy array with given number :: {}".format(fa))
# O/p => NumPy array with given number :: [[4 4 4 4 4]
#                                          [4 4 4 4 4]
#                                          [4 4 4 4 4]]


# 3. arange() - Initialize NumPy arrays with given particular range.
# -------------------------------------------------------------------

ara1 = np.arange(1, 6)
print("NumPy array from range 1 to 6 :: {}".format(ara1))
# O/p => NumPy array from range 1 to 6 :: [1 2 3 4 5]

ara2 = np.arange(1, 50, 3)
print("NumPy array from range 1 to 50 with difference 3 :: {}".format(ara2))
# O/p => NumPy array from range 1 to 50 with difference 3 :: [ 1  4  7 10 13 16 19 22 25 28 31 34 37 40 43 46 49]


# 4. random.randint() - Initialize NumPy arrays with random numbers.
# -------------------------------------------------------------------

rra = np.random.randint(1, 50, 7)
print("Random NumPy array numbers between 1 and 50 :: {}".format(rra))
# O/p => Random NumPy array numbers between 1 and 50 :: [40 31 47 45 17 18 23]


# 5. shape() - returns shape of given array.
#    e.g: (2, 3) - 2 rows and 3 columns
# -------------------------------------------------------------------

sda1 = np.array([[1, 3, 5]])
print("Shape of given NumPy array {} :: {}".format(sda1, sda1.shape))
# O/p => Shape of given NumPy array [[1 3 5]] :: (1, 3)

mda1 = np.array([[1, 3, 5], [2, 4, 6]])
print("Shape of given NumPy array {} :: {}".format(mda1, mda1.shape))
# O/p => Shape of given NumPy array [[1 3 5] :: (2, 3)
#                                    [2 4 6]]


# 6. save() - Saves NumPy arrays.
# --------------------------------

np.save("store_sda", sda)
# Explanation: The above line (Line no. 74) will save NumPy array by generating '{given_file_name}.npy' file locally.


# 7. load() - Loads saved NumPy arrays.
# --------------------------------------

print("Saved '{}' NumPy array :: {}".format("store_sda", np.load("store_sda.npy")))
# O/p => Saved 'store_sda' NumPy array :: [1 2 3 4 5]
