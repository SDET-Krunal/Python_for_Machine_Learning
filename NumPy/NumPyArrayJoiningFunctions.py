import numpy as np

n1 = np.array([1, 3, 5])
n2 = np.array([2, 4, 6])


# NumPy Array joining functions:
# ===============================

# 1. vstack() - Stack two NumPy arrays vertically.
# -------------------------------------------------

vsa = np.vstack((n1, n2))
print("Vertically stacked NumPy arrays :: {}".format(vsa))
# O/p => Vertically stacked NumPy arrays :: [[1 3 5]
#                                            [2 4 6]]


# 2. hstack() - Stack two NumPy arrays horizontally.
# ---------------------------------------------------

hsa = np.hstack((n1, n2))
print("Horizontally stacked NumPy arrays :: {}".format(hsa))
# O/p => Horizontally stacked NumPy arrays :: [1 3 5 2 4 6]


# 3. column_stack() - Stack two NumPy arrays column by column.
# -------------------------------------------------------------

csa = np.column_stack((n1, n2))
print("Column stacked NumPy arrays :: {}".format(csa))
# O/p => Column stacked NumPy arrays :: [[1 2]
#                                        [3 4]
#                                        [5 6]]
