# Ugly Number
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example 1:
# Input:n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:
#   1. 1 is typically treated as an ugly number.
#   2. n does not exceed 1690.

# Solution
# Brute Force
# A brute force method would generate ugly numbers and store all possibilities for look up. We can generate them out
# of order and then sort them later.
#
# In theory this is impossible, but since there are limits on the size of datatypes, we only need to loop up to those
# limits:

def nth_ugly_number(n: int) -> int:
    ugly_numbers = []
    i = 1
    max_int = 2147483647
    while i <= max_int:
        j = i
        while j <= max_int:
            k = j
            while k <= max_int:
                ugly_numbers.append(k)
                k *= 5
            j *= 3
        i *= 2
    ugly_numbers.sort()
    ugly_numbers[n - 1]


# Min Heap

# Instead of generating all the ugly numbers, sorting them, and getting the nth, we can instead generate them in
# order and stop when we get to the nth.
#
# In order to generate them in order, let's consider starting with just the number 1. To generate the next few ugly
# numbers, we can take our 1 and multiply it by 2, 3, and 5, while checking that the newly generated numbers haven't
# been generated yet. Since they have not, we insert them into our list. The new list is now [1, 2, 3, 5].
#
# Next, we'll take the "next element" which is 2. Once again, we take our 2 and multiply it by 2, 3, and 5,
# while checking that the newly generated numbers (4, 6, and 10) haven't been generate yet. The new list,
# in sorted order, is now [1, 2, 3, 4, 5, 6, 10].
#
# The "next element" is 3. Taking 3 and multiplying it by 2, 3, and 5, while checking that 6, 9, and 15 haven't been
# generate yet, we insert them into our list. The new list, in sorted order, is now [1, 2, 3, 4, 5, 6, 9, 10].
#
# Then we deal with 4, then 5, then 6, then 8 (which will be generated from 4), etc...
#
# Continuing this pattern, we see that on the n - 1th iteration, the "next element" that we deal with will be our nth
# ugly number as long as we keep the list in a sorted order. To do so, we can use a min heap which keeps the elements
# in ascending order and will maintain the top most element as the smallest number. Once we finish multiplying the
# smallest number (i.e. the top element in the heap) by 2, 3, and 5, we can pop it from our heap, and now the next
# smallest number will be at the top of the heap. Continuining this cycle, it is clear as to why it works now.
# Lastly, to check if a number has already been generated, we can use a simple hash set.
#
# Below are the first few iterations of the idea above:
#
# First slide
# Previous
# Next
# Below is a solution using this idea.
#
# Time Complexity: O(ans)
#
# Let ans denote the final n-th ugly number. We keep track of each number checked and we never check a number twice.
# Worst case we check every number from 1 to ans resulting in a time complexity of O(ans).

from heapq import heappop, heappush


def nth_ugly_number(n: int) -> int:
    allowed_prime = (2, 3, 5)
    ans_heap = [1]
    used_nums = {1}
    for _ in range(n - 1):
        val = heappop(ans_heap)
        for multiplier in allowed_prime:
            if val * multiplier not in used_nums:
                heappush(ans_heap, val * multiplier)
                used_nums.add(val * multiplier)
    return ans_heap[0]


if __name__ == '__main__':
    n = int(input())
    res = nth_ugly_number(n)
    print(res)
