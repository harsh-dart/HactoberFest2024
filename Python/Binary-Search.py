array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
left = 0
right = len(array) - 1
found = False

while left <= right:
    mid = left + (right - left) // 2
    if array[mid] == target:
        found = True
        break
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if found:
    print("Element found at index:", mid)
else:
    print("Element not found")
