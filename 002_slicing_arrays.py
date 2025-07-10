import numpy as np

list1 = [1,2,3,4,5,6,7,8,9] 
np1 = np.array(list1)
print(np1)

print() 

# slicing
print(f"np1[1:5]: {np1[1:5]} \n")

print(f"np1[3:]: {np1[3:]} \n")

print(f"np1[-3:-1]: {np1[-3:-1]} \n")

print(f"np1[::2]: {np1[::2]} \n")

print(f"np1[::3]: {np1[::3]} \n") 

np2 = np.array([[0,1,2,3,4,5,6,7,8,9], [10,11,12,13,14,15,16,17,18,19] ])
print(np2)
print(np2[1][2])
print(np2[1,2])

print(np2[0:4,2:7]) 