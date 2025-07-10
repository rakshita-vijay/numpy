import numpy as np
 
np1 = np.array([6,1,8,2,4,7,0,2,5,1,3,8,7,3,1,3,6,4,2,9,5,2,1,6])

'''
locations = np.where(np1 == 1)
print(locations)
print(locations[0]) 
print(np1[locations[0]]) 
'''

even_locs = np.where(np1 % 2 == 0)
print(even_locs)
print(np1[even_locs[0]]) 