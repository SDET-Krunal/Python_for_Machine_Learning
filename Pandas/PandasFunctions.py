import pandas as pd

# Pandas Series Object:
# ----------------------

p1 = pd.Series([2, 4, 6, 8, 10])
print("Series value of given list :: {}".format(p1))
# O/p => Series value of given list ::
# 0     2
# 1     4
# 2     6
# 3     8
# 4    10
# dtype: int64


# Change index of Series object values:
# --------------------------------------

p2 = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])
print("Series values after changing index :: {}".format(p2))
# O/p => Series values after changing index ::
# a    1
# b    3
# c    5
# d    7
# e    9
# dtype: int64


# Series object from Dictionary:
# -------------------------------

p3 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print("Series object value after creating from dictionary :: {}".format(p3))
# O/p => Series object value after creating from dictionary ::
# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64


# Change index of Series object created from Dictionary:
# -------------------------------------------------------

p4 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, index=['e', 'd', 'c', 'b', 'a'])
print("Series object value after creating from dictionary :: {}".format(p4))
# O/p => Series object value after creating from dictionary ::
# e    5
# d    4
# c    3
# b    2
# a    1
# dtype: int64


# Extract individual value from created Series object values:
# ------------------------------------------------------------

p5 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8])
print("Extracted value at index '{}' :: {}".format(3, p5[3]))
# O/p => Extracted value at index '3' :: 4
# Explanation: It will extract the value of index '3' and value '4' is at index 3 here as the index starts with '0'.


# Extract sequence of values from created Series object values:
# --------------------------------------------------------------

p6 = pd.Series([2, 4, 6, 8, 10, 12, 14, 16])
print("Extracted values of sequence :: {}".format(p6[:4]))
# O/p => Extracted values of sequence ::
# 0    2
# 1    4
# 2    6
# 3    8
# dtype: int64
# Explanation: It will extract the first four elements.


# Extract values from back of created Series object values:
# ----------------------------------------------------------

p7 = pd.Series([1, 3, 5, 7, 9, 11, 13, 15])
print("Extracted values from back :: {}".format(p7[-3:]))
# O/p => Extracted values from back ::
# 5    11
# 6    13
# 7    15
# dtype: int64
# Explanation: It will extract last three elements.


# Add scalar value to created Series object values:
# --------------------------------------------------

p8 = pd.Series([1, 2, 3, 4, 5])
print("Series object values after adding scalar value '{}' :: {}".format(3, p8 + 3))
# O/p => Series object values after adding '3' ::
# 0    4
# 1    5
# 2    6
# 3    7
# 4    8
# dtype: int64


# Subtract scalar value from created Series object values:
# ---------------------------------------------------------

p9 = pd.Series([2, 4, 6, 8, 10])
print("Series object values after subtracting scalar value '{}' :: {}".format(1, p9 - 1))
# O/p => Series object values after subtracting scalar value '1' ::
# 0    1
# 1    3
# 2    5
# 3    7
# 4    9
# dtype: int64


# Multiply scalar value with created Series object values:
# ---------------------------------------------------------

p10 = pd.Series([2, 4, 6, 8, 10, 12, 14])
print("Series object values after multiplying with scalar value '{}' :: {}".format(4, p10 * 4))
# O/p => Series object values after multiplying with scalar value '4' ::
# 0     8
# 1    16
# 2    24
# 3    32
# 4    40
# 5    48
# 6    56
# dtype: int64


# Divide scalar value by created Series object values:
# -----------------------------------------------------

p11 = pd.Series([1, 3, 5, 7, 9, 11, 13, 15])
print("Series object values after dividing by scalar value '{}' :: {}".format(2, p11 / 2))
# O/p => Series object values after dividing by scalar value '2' ::
# 0    0.5
# 1    1.5
# 2    2.5
# 3    3.5
# 4    4.5
# 5    5.5
# 6    6.5
# 7    7.5
# dtype: float64


# Add created two Series object values:
# --------------------------------------

p12 = pd.Series([1, 3, 5, 7, 9, 11, 13, 15])
p13 = pd.Series([2, 4, 6, 8, 10, 12, 14, 16])
print("Series object values after adding two objects :: {}".format(p12 + p13))
# O/p => Series object values after adding two objects ::
# 0     3
# 1     7
# 2    11
# 3    15
# 4    19
# 5    23
# 6    27
# 7    31
# dtype: int64
