# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Hard

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#
#
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
# Constraints:
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106
from typing import List


class Solution:
    # Time: Log(min(n, m)); running binary search on the smaller array
    # Space: O(1); no data structure is used
    # Logic: find half of total length of 2 lists; run binary search on the shorter length(A), get the middle point of A
    #        and B, and left, right value of A and B; if the partition is correction (A_left <= B_right and B_left <=
    #        A_right): if it's an odd num, return min of either of A_right or B_right; else if it's even, get the min
    #        of (A_right, B_right) and max of (A_left, B_left), then divide 2.
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)     # total length of 2 nums
        half = total // 2                   # half of length

        if len(B) < len(A):  # running binary search on A, ensure A is a smaller array
            A, B = B, A     # swap A, B; since we wanted to run binary search on A
        # run binary search
        l, r = 0, len(A) - 1    # left, right pointer of the binary search on A
        while True:
            i = (l + r) // 2    # middle point; A
            j = half - i - 2    # rest of the half from B; -2 because index are starting 0 (i and j)
            # A_left, B_left: last values at left half arrays;
            # A_right, B_right: beginning values at the right half arrays
            #   set value if inbound else default value
            A_left = A[i] if i >= 0 else float("-infinity")  # if i is inbound(>0) set the value at i else default -inf
            A_right = A[i + 1] if (i + 1) < len(A) else float("infinity")  # if i+1 inbound set val at i+1 else def inf
            B_left = B[j] if j >= 0 else float("-infinity")  # if j is inbound set value at j else default -inf
            B_right = B[j + 1] if (j + 1) < len(B) else float("infinity")   # if j+1 inbound set A[j+1] else default inf

            if A_left <= B_right and B_left <= A_right:  # Partition is correct
                # odd
                if total % 2:   # if total % 2 == 1 (True), odd
                    return min(A_right, B_right)    # min(A_right, B_right) is the middle value for odd length,
                # even
                return (max(A_left, B_left) + min(A_right, B_right)) / 2  # med: (max(left arr) + min(right arr))/ 2
            elif A_left > B_right:  # if left partition of A has too many elements
                r = i - 1   # reduce size of left partition from A
            else:   # B_left > A_right
                l = i + 1   # increase size of left partition from A
