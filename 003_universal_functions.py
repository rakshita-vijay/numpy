import numpy as np

'''
# numpy universal functions
np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)

# square root
print(np.sqrt(np1))

# absolute values
np2 = np.array([0,-1,2,3,-4,5,6,7,-8,9])
print(np.absolute(np2))

# exponential
np3 = np.array([0,-1,2,3,-4,5,6,7,-8,9])
print(np.exp(np3))

# min and max
print("Min number in np3: ", np.min(np3))
print("Max number in np3: ", np.max(np3))

# signs of each digit in np array
print(np.sign(np3))
'''

# trig funtions
np4 = np.array([0,-1,2,3,-4,5,6,7,-8,9,10,11,12,-13])
print("np.sin(np4): ", np.sin(np4), "\n")
print("np.cos(np4): ", np.cos(np4), "\n")
print("np.log(np4): ", np.log(np4), "\n")
# log will throw some error because we have negative values