# First come first serve algorithm 

process = ['p1', 'p2', 'p3', 'p4']
arrival = [3, 0, 5, 2]
burst_time = [4, 7, 2, 3]
waiting = [0] * len(arrival)
turnaround_time = [0] * len(arrival)

def sort_proc():
	for i in range(len(process)):
		for j in range(len(process)-1-i):		
			if(arrival[j] > arrival[j+1]):
				temp = arrival[j]
				arrival[j] = arrival[j+1]
				arrival[j+1] = temp

				temp = process[j]
				process[j] = process[j+1]
				process[j+1] = temp

				temp = burst_time[j]
				burst_time[j] = burst_time[j+1]
				burst_time[j+1] = temp

		
def fcfs():
	sort_proc()
	temp = 0
	for i in range(1, len(arrival)):
		temp = temp + burst_time[i-1]
		waiting[i] = temp - arrival[i]
		
	for i in range(len(arrival)):
		turnaround_time[i] = burst_time[i] + waiting[i]

	total_wt = 0
	total_tat = 0
	for i in range(len(arrival)):
		total_wt += waiting[i]
		total_tat += turnaround_time[i] 


	
	avg_wt = total_wt/len(arrival)
	avg_tat = total_tat/len(arrival)
	
	return avg_wt,avg_tat


if __name__ == '__main__':
	
	avg_wt, avg_tat = fcfs()
	print("Process \t Arrival Time \t Burst Time \t Waiting Time \t Turnaround Time ")
	for i in range(len(arrival)):
		print(str(process[i]) + "\t\t\t\t" + str(arrival[i]) + "\t\t\t\t" + str(burst_time[i]) + "\t\t\t\t" + str(waiting[i]) + "\t\t\t\t" + str(turnaround_time[i]))

	print("\nAverage waiting time: ", avg_wt)
	print("Average turnaround time: ", avg_tat)

	''' EXAMPLE:
    PROCESS-ID   ARRIVAL-TIME   BURST-TIME      
        P1           3             4           
        P2           0             7            
        P3           5             2            
        P4           2             3
    '''