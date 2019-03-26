#Shortest Job First scheduling 

pid = ['p1', 'p2', 'p3', 'p4']
arrival_time = [3, 0, 5, 2]
burst_time = [4, 7, 2, 3]
wait_time = [0]*len(arrival_time)
turnaround_time = [0]*len(arrival_time)

def sort_proc():
    for i in range(len(arrival_time)):
        for j in range(len(arrival_time) - i - 1):
            if(burst_time[j] > burst_time[j+1]):
                temp = burst_time[j]
                burst_time[j] = burst_time[j+1]
                burst_time[j+1] = temp

                temp = arrival_time[j]
                arrival_time[j] = arrival_time[j+1]
                arrival_time[j+1] = temp

                temp = pid[j]
                pid[j] = pid[j+1]
                pid[j+1] = temp


def checkArrived(prev):
    for i in range(len(arrival_time)):
        if(arrival_time[i] <= prev):
            continue
        else:
            return 0
    
    return 1

def btFCFS(prev):
    sort_proc()
    for i in range(len(arrival_time)):
        wait_time[i] = prev - arrival_time[i]
        prev = prev + burst_time[i]
        turnaround_time[i] = burst_time[i] + wait_time[i]


def del_Proc(i):
    del arrival_time[i]
    del burst_time[i]
    del pid[i]



    
def SJF():
    prev = min(arrival_time)
    sort_proc()
    tempPID = pid.copy()
    tempARR = arrival_time.copy()
    tempBT = burst_time.copy()
    
    while(len(arrival_time) != 0):
        if(checkArrived(prev)):
            btFCFS(prev)
            return tempPID, tempARR, tempBT


        for i in range(len(arrival_time)):

            if(arrival_time[i] > prev):
                 j = i 
                 
                 while(arrival_time[j] > prev and j < len(arrival_time)):
                     j += 1
                 
                 if(arrival_time[j] <= prev):
                     wait_time[j] = prev - arrival_time[j]
                     prev = prev + burst_time[j]

                     del_Proc(j)
                
            elif(arrival_time[i] <= prev):
                wait_time[i] = prev - arrival_time[i]
                
                del_Proc(i)

            else:
                k = min(arrival_time)
                while(prev < k):
                    prev = prev + 1
                    
            if(checkArrived(prev)):
                btFCFS(prev)
                return tempPID, tempARR, tempBT

def findAvgTime(tempPID, tempARR, tempBT):
    total_wt = 0
    total_tat = 0

    # displaying process details
    print("The table sorted according to burst time:\n")

    print("Process \t Arrival Time \t Burst Time \t Waiting Time \t Turnaround Time \t")
    for i in range(len(tempPID)):
        print(str(tempPID[i]) + "\t\t\t\t" + str(tempARR[i]) + "\t\t\t\t" + str(tempBT[i]) + "\t\t\t\t" + str(wait_time[i]) + "\t\t\t\t" + str(turnaround_time[i]))

    # calculating total waiting time and total turnaround time
    print("\nAverage waiting time: " + str(sum(wait_time)/len(tempPID)))
    print("Average turnaround time: " + str(sum(turnaround_time)/len(tempPID)))

if __name__ == '__main__':
    tempPID, tempARR, tempBT = SJF()
    findAvgTime(tempPID, tempARR, tempBT)

    ''' EXAMPLE:
    PROCESS-ID   ARRIVAL-TIME   BURST-TIME      
        P1           3             4           
        P2           0             7            
        P3           5             2            
        P4           2             3
    '''