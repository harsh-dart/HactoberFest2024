n = int(input("Enter the number of processes: "))
p = [0] * n
bt = [0] * n
wt = [0] * n
tat = [0] * n
su = [0] * n

# Input burst time and process type
for i in range(n):
    p[i] = i + 1
    bt[i] = int(input("Enter the burst time for process " + str(i + 1) + ": "))
    su[i] = int(input("System/User process (0/1)? "))

# Sort processes based on System/User type
for i in range(n):
    for j in range(i + 1, n):
        if su[i] > su[j]:
            p[i], p[j] = p[j], p[i]
            bt[i], bt[j] = bt[j], bt[i]
            su[i], su[j] = su[j], su[i]

# Calculate waiting time and turnaround time
wt[0] = 0  # First process has no waiting time
tat[0] = bt[0]  # Turnaround time for the first process is its burst time

wtavg = 0
tatavg = 0

for i in range(1, n):
    wt[i] = wt[i - 1] + bt[i - 1]
    tat[i] = tat[i - 1] + bt[i]
    wtavg += wt[i]
    tatavg += tat[i]

# Calculate averages
wtavg /= n
tatavg /= n

# Output results
print("PROCESS\tSYSTEM/USER PROCESS\tBURST TIME\tWAITING TIME\tTURNAROUND TIME")
for i in range(n):
    print(f"{p[i]}\t\t{su[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

print(f"\nAverage Waiting Time: {wtavg:.2f}")
print(f"Average Turnaround Time: {tatavg:.2f}")
