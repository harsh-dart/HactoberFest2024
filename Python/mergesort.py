# Input the number of processes
n = int(input("Enter the number of processes: "))
processes = [0] * n
burst_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n
system_user = [0] * n

# Input burst time and system/user type for each process
for i in range(n):
    processes[i] = i + 1
    burst_time[i] = int(input(f"Enter the burst time for process {i + 1}: "))
    system_user[i] = int(input("System/User process (0/1)? "))

# Sort processes based on system/user type
for i in range(n):
    for j in range(i + 1, n):
        if system_user[i] > system_user[j]:
            processes[i], processes[j] = processes[j], processes[i]
            burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
            system_user[i], system_user[j] = system_user[j], system_user[i]

# Calculate waiting time and turnaround time
waiting_time_avg = 0
turnaround_time_avg = 0

for i in range(1, n):
    waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]
    turnaround_time[i] = turnaround_time[i - 1] + burst_time[i]
    waiting_time_avg += waiting_time[i]
    turnaround_time_avg += turnaround_time[i]

# Print the results
print("PROCESS\tSYSTEM/USER\tBURST TIME\tWAITING TIME\tTURNAROUND TIME")
for i in range(n):
    print(f"{processes[i]}\t\t{system_user[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
