def find_unsorted_subarray(arr):
    n = len(arr)

    # Check if the array is already sorted
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        return [0, 0]

    # Find the first index where the array is not sorted in ascending order
    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1

    # Check if the array is already sorted in descending order
    if left == n - 1:
        return [0, 0]

    # Find the last index where the array is not sorted in ascending order
    right = n - 1
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1

    # Find the minimum and maximum values in the unsorted subarray
    min_val = min(arr[left:right + 1])
    max_val = max(arr[left:right + 1])

    # Expand the unsorted subarray to include all elements less than min_val
    while left >= 0 and arr[left] > min_val:
        left -= 1

    # Expand the unsorted subarray to include all elements greater than max_val
    while right < n and arr[right] < max_val:
        right += 1

    return [left + 1, right - 1]

# Example usage:
arr = [1, 2, 3, 6, 4, 4]
result = find_unsorted_subarray(arr)
print(result)  # Output: [3, 5]
