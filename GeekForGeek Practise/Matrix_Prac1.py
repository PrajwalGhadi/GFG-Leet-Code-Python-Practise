'''Date - 11-06-2021
Author - Prajwal Ghadi
Aim - Python – Assigning Subsequent Rows to Matrix first row elements.
                                and
    Adding and Subtracting Matrices in Python.'''

import numpy as np
a = [[3, 4, 5], [3, 5, 7], [1, 5, 8]]
new = {a[0][ele]: a[ele - 1] for ele in range(len(a) - 1)}
print(new)

# Adding and Substracting Matrices in python
b = [[1, 3, 5], [7, 2, 8]]
c = [[2, 6, 4], [8, 1, 9]]

print('Adding of 2 Array', np.add(b, c))
print('Substraction of 2 Array', np.subtract(b, c))