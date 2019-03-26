# Program for first fit scheme

block_size = [300, 150, 400, 650, 500]

def display(pid, required, arr):
	print('Process \t Process Size \t Block Allocated')
	for i in range(len(pid)):
		print(str(pid[i]) + "\t\t\t\t" + str(required[i]) + "\t\t\t\t" + str(arr[i]+1))
	print("\n\nIf allocated block = 0 => memory block not allocated.\n")

def firstFit(required,allocation):
	for i in range(len(required)):
		for j in range(len(block_size)):
			if(block_size[j] >= required[i]):
				allocation[i] = j				# allocate block j to process i
				block_size[j] -= required[i]	# reduce available memory in block
				break
	

if __name__ == "__main__":
# The block of code below is to be used if the process requirement is user defined	
	# pid = []
	# mem_required = []
	# print("Enter number of processes: ")
	# n = int(input())

	# for i in range(n):
	# 	p = "P" + str(i+1)
	# 	pid.append(p)

	# print("Enter memory required for each process: ")
	# for i in range(n):
	# 	a = int(input())
	# 	mem_required.append(a)


	pid = ['P1', 'P2', 'P3', 'P4']
	mem_required = [127, 443, 555, 325]
	allocation = [-1] * len(pid)

	print("Memory block \t Block size")
	for i in range(len(block_size)):
		print(str(i+1) + "\t\t\t\t\t" + str(block_size[i]))
	print("\n============================================\n")

	firstFit(mem_required,allocation)
	display(pid, mem_required, allocation)