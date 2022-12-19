# Sliding Window Median (hard)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744001784_63Unit

# Problem Statement
#
# Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
#
# Example 1:
# Input: nums=[1, 2, -1, 3, 5], k = 2
# Output: [1.5, 0.5, 1.0, 4.0]
# Explanation: Lets consider all windows of size ‘2’:
#   * [1, 2, -1, 3, 5] -> median is 1.5
#   * [1, 2, -1, 3, 5] -> median is 0.5
#   * [1, 2, -1, 3, 5] -> median is 1.0
#   * [1, 2, -1, 3, 5] -> median is 4.0
#
# Example 2:
# Input: nums=[1, 2, -1, 3, 5], k = 3
# Output: [1.0, 2.0, 3.0]
# Explanation: Lets consider all windows of size ‘3’:
#   * [1, 2, -1, 3, 5] -> median is 1.0
#   * [1, 2, -1, 3, 5] -> median is 2.0
#   * [1, 2, -1, 3, 5] -> median is 3.0

# Solution
#
# This problem follows the Two Heaps pattern and share similarities with Find the Median of a Number Stream. We can
# follow a similar approach of maintaining a max-heap and a min-heap for the list of numbers to find their median.
#
# The only difference is that we need to keep track of a sliding window of ‘k’ numbers. This means,
# in each iteration, when we insert a new number in the heaps, we need to remove one number from the heaps which is
# going out of the sliding window. After the removal, we need to rebalance the heaps in the same way that we did
# while inserting.

from heapq import *
import heapq


class SlidingWindowMedian:
    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for x in range(len(nums) - k + 1)]
        for i in range(0, len(nums)):
            if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])

            self.rebalance_heaps()

            if i - k + 1 >= 0:  # if we have at least 'k' elements in the sliding window
                # add the median to the the result array
                if len(self.maxHeap) == len(self.minHeap):
                    # we have even number of elements, take the average of middle two elements
                    result[i - k + 1] = -self.maxHeap[0] / \
                                        2.0 + self.minHeap[0] / 2.0
                else:  # because max-heap will have one more element than the min-heap
                    result[i - k + 1] = -self.maxHeap[0] / 1.0

                # remove the element going out of the sliding window
                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -elementToBeRemoved)
                else:
                    self.remove(self.minHeap, elementToBeRemoved)

                self.rebalance_heaps()

        return result

    # removes an element from the heap keeping the heap property
    def remove(self, heap, element):
        ind = heap.index(element)  # find the element
        # copy the last element of the heap to this index and decrement the heap size
        heap[ind] = heap[-1]
        del heap[-1]

        # adjust the position of the element while maintaining the heap property.
        # we can use heapify to readjust the elements but that would be O(N),
        # instead, we will adjust only one element which will O(logN)
        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)

    def rebalance_heaps(self):
        # either both the heaps will have equal number of elements or max-heap will have
        # one more element than the min-heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))


def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()

# Time Complexity
#
# The time complexity of our algorithm is O(N∗K) where ‘N’ is the total number of elements in the input array
# and ‘K’ is the size of the sliding window. This is due to the fact that we are going through all the ‘N’ numbers
# and, while doing so, we are doing two things:
#   1. Inserting/removing numbers from heaps of size ‘K’. This will take O(logK).
#   2. Removing the element going out of the sliding window. This will take O(K) as we will be searching this element in
#      an array of size ‘K’ (i.e., a heap).

# Space Complexity
# Ignoring the space needed for the output array, the space complexity will be O(K) because, at any time,
# we will be storing all the numbers within the sliding window.
