import numpy as np
'''
# create 1d np array and get shape
np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)

# create 2d np array and get shape

np2 = np.array([[0,1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19]])
print(np2)
print(np2.shape)

# re-shape to 2d np array
np3 = np1.reshape(2,5)
print(np3)

np4 = np1.reshape(5,2)
print(np4)
'''

# re-shape to 3d np array
np5 = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
np6 = np5.reshape(2,3,2)
print(np6) 
print(np6.shape)

# flatten to 1d
np7 = np6.reshape(-1)
print(np7)
print(np7.shape)