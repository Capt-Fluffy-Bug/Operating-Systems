# Banker's algorithm

import numpy as np

# assuming number of available resources = number of processes = 3
r = 3
p =3


def callBanker(available, maximum, allocated, need):
	work = available.copy()
	finish = [0] * p
	safeSeq = [0] * p
	count = 0

	# while all processes haven't finished
	while(count < p):
		# to find an unfinished process that satisfies conditions
		found = 0

		for i in range(p):
			if(finish[i] == 0):
				for j in range(r):
					if(need[i][j] > work[j]):
						break

					if(j == r-1):
						for k in range(r):
							work[k] += allocated[i][k]

						safeSeq[count] = i
						count = count + 1

						finish[i] = 1
						found = 1

		if(found == 0):
			print("\nSystem is unsafe.\n\n")
			return False

	print("\nSystem is safe")
	print("\nSafe sequence: ", *safeSeq)
	print("\n\n")

	return True




if __name__ == '__main__':


	# number of resources available in the system
	available = np.asarray([1, 2, 3])

	# the amount of resources a process requires at the max
	maximum = np.asarray([[2, 5, 1], [1, 3, 3], [3, 2, 1]])

	# the amount of resources already allocated to a process		  
	allocated = np.asarray([[0, 4, 1], [1, 3, 0], [2, 2, 0]])

	# the amount of resources required by a process to complete execution
	need = np.subtract(maximum, allocated) 

	print("Available: \n", *available)
	print("\nMaximum: \n", *maximum)
	print("\nAllocated: \n", *allocated)
	print("\nNeed: \n", *need)

	callBanker(available, maximum, allocated, need)
