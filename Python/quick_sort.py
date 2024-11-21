def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Test cases
def test_quick_sort():
    assert quick_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10], "Test case 1 failed"
    assert quick_sort([10, 7, 8, 9, 1, 5]) == [1, 5, 7, 8, 9, 10], "Test case 2 failed"
    assert quick_sort([]) == [], "Test case 3 failed"  # empty list
    assert quick_sort([1]) == [1], "Test case 4 failed"  # single element
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 5 failed"  # already sorted
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Test case 6 failed"  # reverse sorted

    print("All test cases passed!")

# Run test cases
test_quick_sort()
