#Priority scheduling algorithm

def sort_proc(arrival_time, burst_time, priority, pid):
    for i in range(len(arrival_time)):
        for j in range(len(arrival_time) - i - 1):
            if(priority[j] > priority[j+1]):
                temp = priority[j]
                priority[j] = priority[j+1]
                priority[j+1] = temp

                temp = burst_time[j]
                burst_time[j] = burst_time[j+1]
                burst_time[j+1] = temp

                temp = arrival_time[j]
                arrival_time[j] = arrival_time[j+1]
                arrival_time[j+1] = temp

                temp = pid[j]
                pid[j] = pid[j+1]
                pid[j+1] = temp

    return arrival_time,burst_time,priority,pid


def checkArrived(arrival_time, prev):
    for i in range(len(arrival_time)):
        if(arrival_time[i] <= prev):
            continue
        else:
            return 0
    
    return 1

def priorityFCFS(arrival_time, burst_time, priority, pid, count, turnaround_time, prev):
    arrival_time,burst_time,priority,pid = sort_proc(arrival_time, burst_time, priority, pid)
    for i in range(len(arrival_time)):
        
        if(count == 0):
        
            count  = 1
            wait_time[i] = prev - arrival_time[i]
            prev = prev + burst_time[i]
            turnaround_time[i] = burst_time[i] + wait_time[i]
                        
        else:
            wait_time[i] = prev - arrival_time[i]
            turnaround_time[i] = burst_time[i] + wait_time[i]                   
            prev = prev + burst_time[i]

            
        
    
    


def del_proc(i, arrival_time, burst_time, priority, pid, wait_time):

    del arrival_time[i]
    del burst_time[i]
    del priority[i]
    del pid[i]
    
    return arrival_time, burst_time, priority, pid

def prioritySchedule(arrival_time, burst_time, priority, pid, wait_time):
    arrival_time,burst_time,priority,pid = sort_proc(arrival_time, burst_time, priority, pid)
    prev = min(arrival_time)
    tempPID = pid.copy()
    tempARR = arrival_time.copy()
    tempBT = burst_time.copy()
    tempPR = priority.copy() 
    count = 0
    # st = [0]*len(arrival_time)
    # ft = [0]*len(arrival_time)
    turnaround_time = [0]*len(arrival_time)

    while(len(arrival_time) != 0):
        
        if(checkArrived(arrival_time, prev)):
            priorityFCFS(arrival_time, burst_time, priority, pid, count, turnaround_time, prev)
            return wait_time, turnaround_time, tempPID, tempARR, tempBT, tempPR

        for i in range(len(arrival_time)):
            
            
            if(arrival_time[i] <= prev):
                
                if(count == 0):
                    st[i] = arrival_time[i] 
                    wait_time[i] = prev - arrival_time[i]
                    prev = prev + burst_time[i]
                    count = 1
                   # print("Waiting time for prcoess",pid[i],"is :",wait_time[i])
        
                    turnaround_time[i] = burst_time[i] + wait_time[i]
                    
                else:
                    wait_time[i] = prev - arrival_time[i]
                    turnaround_time[i] = burst_time[i] + wait_time[i]                   
                    prev = prev + burst_time[i]
                   # print("Waiting time for prcoess",pid[i],"is :",wait_time[i])
                arrival_time,burst_time,priority,pid = del_proc(i, arrival_time, burst_time, priority, pid, wait_time)
            elif(arrival_time[i] > prev):
                
                j = i
                while(arrival_time[j] > prev and j<len(arrival_time)):
                    j = j + 1
                k = min(arrival_time)
                while(k > prev):
                    prev = prev + 1
                if(arrival_time[j] <= prev):
                    
                    if(count == 0):
                        count = 1
                        wait_time[j] = prev - arrival_time[j]
                        prev = prev + burst_time[j]
                        turnaround_time[i] = burst_time[i] + wait_time[i]
                    else:
                        wait_time[j] = prev - arrival_time[j]
                        turnaround_time[i] = burst_time[i] + wait_time[i]                   
                        prev = prev + burst_time[j]
                    arrival_time,burst_time,priority,pid = del_proc(j, arrival_time, burst_time, priority, pid, wait_time)
            if(checkArrived(arrival_time, prev)):
                priorityFCFS(arrival_time, burst_time, priority, pid, count, turnaround_time, prev)
                return wait_time, turnaround_time, tempPID, tempARR, tempBT, tempPR
            
    
    return wait_time,turnaround_time,temp_pid
 
def findAvgTime(tempPID, tempARR, tempBT, tempPR):
    total_wt = 0
    total_tat = 0

    # displaying process details
    print("The table sorted according to priority:\n")

    print("Process \t Arrival Time \t Burst Time \t Priority \t Waiting Time \t Turnaround Time \t")
    for i in range(len(tempPID)):
        print(str(tempPID[i]) + "\t\t\t\t" + str(tempARR[i]) + "\t\t\t\t" + str(tempBT[i]) + "\t\t\t\t" + str(tempPR[i]) + "\t\t\t\t" + str(wait_time[i]) + "\t\t\t\t" + str(turnaround_time[i]))

    # calculating total waiting time and total turnaround time
    print("\nAverage waiting time: " + str(sum(wait_time)/len(tempPID)))
    print("Average turnaround time: " + str(sum(turnaround_time)/len(tempPID)))


pid = ['p1', 'p2', 'p3', 'p4']
arrival_time = [3, 0, 5, 2]
burst_time = [4, 7, 2, 3]
wait_time = [0]*len(arrival_time)
priority = [2, 4, 3, 1]

if __name__ == '__main__':
    wait_time, turnaround_time, tempPID, tempARR, tempBT, tempPR = prioritySchedule(arrival_time, burst_time, priority, pid, wait_time)
    findAvgTime(tempPID, tempARR, tempBT, tempPR)

''' EXAMPLE:
PROCESS-ID   ARRIVAL-TIME   BURST-TIME      
    P1           3             4           
    P2           0             7            
    P3           5             2            
    P4           2             3
'''