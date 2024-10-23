# solving  0/1 knapsack problem using branch and bound
# Function to solve 0/1 Knapsack problem with backtracking 
def knapsack_backtracking(weights,values,capacity,n): 
    stack=[(0,0,0,[])] 
    best_value=0 
    best_items=[] 
    while stack: 
        current_index,current_weight,current_value,included_items=stack.pop() 
        if current_index==n: 
            if current_value>best_value: 
                best_value=current_value 
                best_items=included_items[:] 
            continue 
        stack.append((current_index+1,current_weight,current_value,included_items[:])) 
 
 
        if current_weight+weights[current_index]<=capacity: 
            new_list=included_items[:] 
            new_list.append(current_index) 
            stack.append((current_index+1,current_weight+weights[current_index],current_value+values
 [current_index],new_list)) 
    print("Items included (0-indexed):", best_items) 
    return best_value 
n=int(input('Enter number of items:')) 
weights=[] 
values=[] 
for i in range(n): 
    x=int(input(f"Enter weight of item-{i}:")) 
    weights.append(x) 
    y=int(input(f"Enter profit of item-{i}:")) 
    values.append(y) 
print('weights:',weights) 
print('Values/profits:',values) 
capacity=int(input('Enter knapsack capacity:')) 
max_value=knapsack_backtracking(weights,values,capacity,n) 
print('The max profit is:',max_value)
