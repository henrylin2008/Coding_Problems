# 27. Remove Element
#
# https://leetcode.com/problems/remove-element/
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example 1:
#
# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2, with the first two elements of nums being 2.
#
# It doesn't matter what you leave beyond the returned length.
# Example 2:
#
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
#
# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
#
# Note that the order of those five elements can be arbitrary.
#
# It doesn't matter what values are set beyond the returned length.
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
#
# Internally you can think of this:
#
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeElement(nums, val);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

def removeElement(nums, val):

    # logic: create 2 pointers: beginning of nums and last of nums
    # swap 1st and last
    # For Ex 1: [3,2,2,3], val = 3
    # round 1 (after swap): 3, 2, 2, 3 (swapped nums[0] (first) and nums[3] (last); last pointer: nums[2] = 2)
    # round 2 (after swap): 2, 2, 3, 3 (swapped nums[0] (first) and nums[2] (second to last); last pointer: nums[1] = 2)
    # Initial pointer (i), check first and second number, both are not the value to remove
    # round 3: 2, 2, 3, 3 (nums[0]=2, not the removal value, stay the same)
    # round 4: 2, 2, 3, 3 (nums[1]=2, not the removal value, stay the same, initial pointer (i) at nums[1])
    # round 5: initial pointer (i: nums[1], last pointer: nums[1]); return last (pointer) + 1

    i, last = 0, len(nums) -1  # set initial pointer and last pointer

    while i <= last: # while initial pointer <= last pointer
        if nums[i] == val: # when value of nums[i] equals (removal) value
            nums[i], nums[last] = nums[last], nums[i] # swap num[i] with last (index) value
            last -= 1 # move last pointer one position to the left
        else:
            i += 1 # increase the index (until it meets last pointer)
    return last+1  # adding ones b/c index starts at 0