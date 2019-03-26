# Round Robin Scheduling Algorithm

def sort_proc(pid, arrival_time, burst_time):
    for j in range(len(arrival_time)):
        for k in range(len(arrival_time) - j - 1):
            if(arrival_time[k] > arrival_time[k+1]):
                temp = burst_time[k]
                burst_time[k] = burst_time[k+1]
                burst_time[k+1] = temp

                temp = arrival_time[k]
                arrival_time[k] = arrival_time[k+1]
                arrival_time[k+1] = temp

                temp = pid[k]
                pid[k] = pid[k+1]
                pid[k+1] = temp

    return pid, arrival_time, burst_time


def RR(pid, arrival_time, burst_time, quantum):
	pid, arrival_time, burst_time = sort_proc(pid, arrival_time, burst_time)
	tempARR = arrival_time.copy()
	n = len(pid)

	wait_time = [0] * len(arrival_time)
	prev = [0] * len(arrival_time)
	turnaround_time = [0]*len(arrival_time)

	seq = []
	rem_time = burst_time.copy()

	total = 0
	t = 0
	flag = 0
	i = 0
	k = 0
	
	while(1):
		if(i == n):
			i = 0
		if(flag == n):
			break

		if(rem_time[i] <= quantum and rem_time[i] > 0):
			wait_time[i] += total - prev[i]
			flag += 1
			total += rem_time[i]
			rem_time[i] = 0
			seq.append(pid[i])
			k += 1

		if(rem_time[i] > quantum):
			wait_time[i] += total - prev[i]
			rem_time[i] = rem_time[i] - quantum
			total += quantum
			seq.append(pid[i])
			k += 1

		prev[i] = total
		i += 1

	for i in range(n):
		turnaround_time[i] = wait_time[i] + burst_time[i]

	return wait_time, turnaround_time, seq

def findAvgTime(wait_time, turnaround_time):
    total_wt = 0
    total_tat = 0

    # calculating total waiting time and total turnaround time
    print("\nAverage waiting time: " + str(sum(wait_time)/len(wait_time)))
    print("Average turnaround time: " + str(sum(turnaround_time)/len(turnaround_time)))

			
if __name__ == '__main__':

	# process details
	pid = ['p1', 'p2', 'p3', 'p4']
	arrival_time = [3, 0, 5, 2]
	burst_time = [4, 7, 2, 3]

	# setting value of time quantum 
	quantum = 2

	wait_time, turnaround_time, seq = RR(pid, arrival_time, burst_time, quantum)

	print("time quantum = ", quantum, "ms")
	# displaying process details
	print("\nThe table sorted according to arrival time:\n")

	print("Process \t Arrival Time \t Burst Time \t Waiting Time \t Turnaround Time")
	for i in range(len(pid)):
		print(str(pid[i]) + "\t\t\t\t" + str(arrival_time[i]) + "\t\t\t\t" + str(burst_time[i]) + "\t\t\t\t" + str(wait_time[i]) + "\t\t\t\t" + str(turnaround_time[i]))
	
	findAvgTime(wait_time, turnaround_time)

	print("\nSequence: ",seq)


''' EXAMPLE:
PROCESS-ID   ARRIVAL-TIME   BURST-TIME      
    P1           3             4           
    P2           0             7            
    P3           5             2            
    P4           2             3
'''
