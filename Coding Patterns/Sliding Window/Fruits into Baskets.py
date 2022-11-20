# Fruits into Baskets (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541018393_2Unit

# Problem Statement
# You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets,
# and your goal is to pick as many fruits as possible to be placed in the given baskets.
#
# You will be given an array of characters where each character represents a fruit tree. The farm has the following
# restrictions:
#   1. Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
#   2. You can start with any tree, but you can’t skip a tree once you have started.
#   3. You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from
#      a third fruit type.
# Write a function to return the maximum number of fruits in both baskets.

# Example 1:
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
#
# Example 2:
# Input: Fruit = ['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the
# second letter: ['B', 'C', 'B', 'B', 'C']

# Solution
# This problem follows the Sliding Window pattern and is quite similar to Longest Substring with K Distinct
# Characters. In this problem, we need to find the length of the longest subarray with no more than two distinct
# characters (or fruit types!). This transforms the current problem into Longest Substring with K Distinct Characters
# where K=2.

def fruits_into_baskets(fruits):
    window_start = 0
    max_length = 0
    fruit_frequency = {}

    # try to extend the range [window_start, window_end]
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        # shrink the sliding window, until we are left with '2' fruits in the fruit
        # frequency dictionary
        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1  # shrink the window
        max_length = max(max_length, window_end-window_start + 1)
    return max_length


def main():
    print("Maximum number of fruits: "
          + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))    # 3
    print("Maximum number of fruits: "
          + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))   # 5


main()

# Time Complexity
# The above algorithm’s time complexity will be O(N), where ‘N’ is the number of characters in the input array. The
# outer 'for' loop runs for all characters, and the inner 'while' loop processes each character only once; therefore,
# the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to O(N).
#
# Space Complexity
# The algorithm runs in constant space O(1) as there can be a maximum of three types of fruits stored in the
# frequency map.
