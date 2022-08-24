# Merge K Sorted Lists
# link: https://algo.monster/problems/merge_k_sorted_lists

# Given k sorted lists of numbers, merge them into one sorted list.
#
# Input: [[1, 3, 5], [2, 4, 6], [7, 10]]
#
# Output: [1, 2, 3, 4, 5, 6, 7, 10]


# Explanation
# Intuition
# The first thing that comes to mind is we can concatenate all the lists into one and sort the list. This is O(N log(
# N))) because sorting is O(N log(N)) where N is the total length of all lists.
#
# Next, we ask the question "are there any conditions that we haven't used?". We know that all the lists are sorted
# and we haven't used that condition. For each list, the smallest number is the first number. We can take the first
# number of each list and put them into a "pool of top k smallest numbers", where k is the number of lists. The
# smallest number in the pool is the smallest number of all the lists and should be added to the final merged list.
# We then take the next smallest number from the list and add it to the pool. Repeat until we have exhausted all the
# lists.
#
# Now the question becomes "how do we compare a stream of k numbers?", and that's a perfect use case for a min heap.
