# Maximum Sum Subarray of Size K (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1627871358579_1Unit

# Problem Statement
#
# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of
# size ‘k’.
#
# Example 1:
# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
#
# Example 2:
# Input: [2, 3, 4, 1, 5], k=2
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

# If you observe closely, you will realize that to calculate the sum of a contiguous subarray, we can utilize the sum
# of the previous subarray. For this, consider each subarray as a Sliding Window of size ‘k.’ To calculate the sum of
# the next subarray, we need to slide the window ahead by one element. So to slide the window forward and calculate
# the sum of the new position of the sliding window, we need to do two things:
#   1. Subtract the element going out of the sliding window, i.e., subtract the first element of the window.
#   2. Add the new element getting included in the sliding window, i.e., the element coming right after the end of the
#   window.

# This approach will save us from re-calculating the sum of the overlapping part of the sliding window. Here is what
# our algorithm will look like:
def max_sub_array_of_size_k(k, arr):
    max_sum, window_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        # slide the window, no need to slide if we've not hit the required window size of 'k'
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead
    return max_sum


def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()


# Time Complexity
# The time complexity of the above algorithm will be O(N).
#
# Space Complexity
# The algorithm runs in constant space O(1).
