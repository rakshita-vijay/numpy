import numpy as np

np1 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])

'''
for x in np1:
	for y in x:
		for z in y:
			print(z)
'''

for x in np.nditer(np1):
	print(x)