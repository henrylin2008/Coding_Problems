# Daily Coding Problem #2
# Problem
# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of
# all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
# [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?
#
# Solution
# This problem would be easy with division: an optimal solution could just find the product of all numbers in the array
# and then divide by each of the numbers.
#
# Without division, another approach would be to first see that the ith element simply needs the product of numbers
# before i and the product of numbers after i. Then we could multiply those two numbers to get our desired product.
#
# In order to find the product of numbers before i, we can generate a list of prefix products. Specifically, the ith
# element in the list would be a product of all numbers including i. Similarly, we would generate the list of suffix
# products. Finally, for each index we can multiply the appropriate prefix and suffix values to obtain our solution.

# Time: O(n)
# Space: O(n)
# since iterating over the input arrays takes O(N) time and creating the prefix and suffix arrays take up O(N) space.
def productsExceptSelf(nums):
    # Generate prefix products
    prefix_products = []
    for n in nums:
        if prefix_products:  # new num = current num * last num, and append it to the prefix_products list
            prefix_products.append(prefix_products[-1] * n)
        else:  # append first item in nums list to prefix_products list
            prefix_products.append(n)

    # Generate suffix products
    suffix_products = []
    for n in reversed(nums):
        if suffix_products:  # new num = current num * last num, and append it to the suffix_products list
            suffix_products.append(suffix_products[-1] * n)
        else:  # append reversed first item/last item into suffix_products list
            suffix_products.append(n)
    suffix_products = list(reversed(suffix_products))  # converted it to a list

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:  # first num in nums
            result.append(suffix_products[i + 1])  # second value: [120]
        elif i == len(nums) - 1:  # last num in nums
            result.append(prefix_products[i - 1])  # second to last value: [24]
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
            # prefix_products: [1,2,6,24,120] ==> [1,2,6]
            # suffix_products: [120,120,60,20,5] ==> [60,20,5]
            # result = [1st in if, 1*60=60, 2*20=40, 6*5=30, last in elif]
    return result

# Solution 2:
# Iterate from left to right, calculating the product of all numbers to the left. The iterate from right to left,
# multiplying each result by the product of all numbers to the right. If any one value is zero then result is all
# zeros apart from that entry.
# Time: O(n)
# Space: O(1)
#
# def productsExceptSelf(nums):
#
#     products = [1]    # product of all to left of nums[0] is set to 1
#     for i in range(1, len(nums)):
#         products.append(nums[i - 1] * products[-1])
#
#     right_product = 1
#     for i in range(len(nums) - 1, -1, -1):
#         products[i] *= right_product
#         right_product *= nums[i]
#
#     return products
