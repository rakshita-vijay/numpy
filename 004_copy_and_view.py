import numpy as np

np1 = np.array([0,1,2,3,4,5,6,7,8,9])

np2 = np1.view()

print(f"Original np1: {np1}")
print(f"Original np2: {np2} \n")

np2[0] = 666
np1[0] = -333

print(f"Changed np1: {np1}")
print(f"Original np2: {np2} \n")

print("~~~~~~~~~~~~ \n")

np3 = np.array([0,1,2,3,4,5,6,7,8,9])

np4 = np3.copy()

print(f"Original np3: {np3}")
print(f"Original np4: {np4} \n")

np3[0] = 666

print(f"Changed np3: {np3}")
print(f"Original np4: {np4} \n")