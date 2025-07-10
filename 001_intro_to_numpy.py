import numpy as np
 
list1 = [1,2,3,4,5]
list2 = ["John", 1, 2.34, True]

np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)

# range
np2 = np.arange(10)
print(np2) 

# step
np3 = np.arange(0, 10, 2)
print(np3) 

# zeroes
np4 = np.zeros(10)
print(np4) 

# multidimensional zeroes
np5 = np.zeros((2, 10))
print(np5)

# full - because we don't want zeroes
np6 = np.full(10, 6)
print(np6)

# multidimensional full 
np7 = np.full((2, 10), 6)
print(np7) 