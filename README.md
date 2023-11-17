# Flask-Kata-1

## Problem Statement
Given an array of integers, arr, find two indices m and n (0 <= m <= len(arr)-1, 0 <= n <= len(arr)-1, m <= n), such that as long as all elements in the subarray (from index m to n, inclusive) are sorted properly, with this sorted subarray replacing the original subarray, the whole array is sorted (either ascendingly or descendingly).

The subarray should include the least number of elements, meaning (n-m) must be of the smallest value, and n should also be the smallest one.

The function should accept an array of integers, arr, and return the subarray's start and end index in array format, [m, n] as a result.

## Example
For an array [1,2,3,6,4,4], the smallest (with the least number of integers) subarray to be found is [6,4,4]. If we sort it to [4,4,6], then replace the original subarray, the whole array now turns to be [1,2,3,4,4,6], which is sorted completely. This subarray begins from index 3 and ends in index 5, so the result is [3, 5].

If all elements in the array are the same, return array [0,0]. If all elements in the array are already sorted, no matter ascendingly or descendingly, return [0,0] as well.

## Usage
```python
arr = [1, 2, 3, 6, 4, 4]
result = find_unsorted_subarray(arr)
print(result)  # Output: [3, 5]
```

## Notes
- The given array can contain positive and negative integers.
- The function should handle cases where the array is already sorted.
- The function should handle cases where all elements in the array are the same.