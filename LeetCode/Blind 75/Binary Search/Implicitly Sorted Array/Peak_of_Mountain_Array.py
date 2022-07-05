# The Peak of a Mountain Array
# https://algo.monster/problems/peak_of_mountain_array

# A mountain array is defined as an array that
#  -has at least 3 elements
#  -has an element with the largest value called "peak", with index k. The array elements monotonically increase from
#  the first element to A[k], and then monotonically decreases from A[k + 1] to the last element of the array. Thus
#  creating a "mountain" of numbers.
#
# That is, given A[0]<...<A[k-1]<A[k]>A[k+1]>...>A[n-1], we need to find the index k. Note that the peak element is
# neither the first nor the last element of the array.
#
# Find the index of the peak element. Assume there is only one peak element.
#
# Input: 0 1 2 3 2 1 0
#
# Output: 3
#
# Explanation: the largest element is 3 and its index is 3.


from typing import List


# Note: The peak element is always larger than the next element. Applying the filter of arr[i] > arr[i + 1] we get a
# boolean array. A minor edge case is for the last element as it has no next element. In that case, we assume its
# next element is negative infinity.
#
#   0   1   2   3   2   1   0   [-inf]
#               ||
#               vv
#        arr[i] > arr[i + 1]
#               ||
#               vv
#   F   F   F   T   T   T   T
#
# Now the problem is reduced to finding the first true element in a boolean array.

# Time: O(log(n))

def peak_of_mountain_array(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)


# Test #1
# Input
# 0 1 2 3 2 1 0
# Output
# 3

# Test #2
# Input
# 0 10 3 2 1 0
# Output
# 1

# Test #3
# Input
# 0 10 0
# Output
# 1

# Test #4
# Input
# 0 1 2 12 22 32 42 52 62 72 82 92 102 112 122 132 133 132 111 0
# Output
# 16

