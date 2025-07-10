import numpy as np

np1 = np.array([i for i in range(1,11)])

# x = [True, True, False, False, False, False, False, False, False, False]

# print(np1[x])

filtered_list = []

for thing in np1:
	if thing % 2 == 0: 
		filtered_list.append(True)
	else:
		filtered_list.append(False)

print(np1[filtered_list])