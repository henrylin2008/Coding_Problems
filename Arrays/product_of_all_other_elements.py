# Daily Coding Problem #2
# Problem
# This problem was asked by Uber.
# Link: https://binarysearch.com/problems/Special-Product-Array

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
# Iterating over the input arrays takes O(N) time and creating the prefix and suffix arrays take up O(N) space.
def productsExceptSelf(nums):
    # Generate prefix products
    # if nums = [1,2,3,4,5]
    prefix_products = []
    for n in nums:
        if prefix_products:  # new num = current num * previous num, and append it to the prefix_products list
            prefix_products.append(prefix_products[-1] * n)  # i=2,3,4,5: [2*1=2, 3*2=6, 4*6=24, 5*24=120]
        else:  # append first item in nums list to prefix_products list
            prefix_products.append(n)   # i=1: [1]
    # prefix_products: [1,2,6,24,120]

    # Generate suffix products
    suffix_products = []
    for n in reversed(nums):
        # n= 5,4,3,2,1
        if suffix_products:  # new num = current num * previous num, and append it to the suffix_products list
            suffix_products.append(suffix_products[-1] * n)     # n=4,3,2,1 => [4*5=20, 3*20=60, 2*60=120, 1*120=120]
        else:  # append reversed first item/previous item into suffix_products list
            suffix_products.append(n)   # n=5 => [5]
        # suffix_products: [5,20,60,120,120]
    suffix_products = list(reversed(suffix_products))  # reverse suffix_products and convert it to a list
    # suffix_products after reversed: [120,120,60,20,5]

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:  # first num in nums
            result.append(suffix_products[i + 1])  # suffix_products[1]: [120]
        elif i == len(nums) - 1:  # last num in nums
            result.append(prefix_products[i - 1])  # prefix_products[3]: [24]
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
            # prefix_products: [1,2,6,24,120];   suffix_products: [120,120,60,20,5]
            # index: prefix_products  *  suffix_products   =    result
            # 1    : [1-1]=0 => 1        [1+1]=2 => 60     ==> [120(above), 60]
            # 2    : [2-1]=1 => 2        [2+1]=3 => 20     ==> [120, 60, 40]
            # 3    : [3-1]=2 => 6        [3+1]=4 => 5      ==> [120, 60, 40, 30]
            # 4    : (above)                               ==> [120, 60, 40, 30, 24]
    return result

# Solution 2:
# Iterate from left to right, calculating the product of all numbers to the left. The iterate from right to left,
# multiplying each result by the product of all numbers to the right. If any one value is zero then result is all
# zeros apart from that entry.
# Time: O(n)
# Space: O(1)
# def productsExceptSelf(nums):
#     products = [1]    # product of all to left of nums[0] is set to 1
#     for i in range(1, len(nums)): # products from left to right
#         products.append(nums[i - 1] * products[-1])   # products: [1,1,2,6,24]
#
#     right_product = 1
#     for i in range(len(nums) - 1, -1, -1):    # products from right to left
#         products[i] *= right_product      # 24*1=24, 6*5=30, 2*20=40, 1*60=60, 1*120=120
#         right_product *= nums[i]      # 1*5=5, 5*4=20, 20*3=60, 60*2=120, 120*1=120
#
#     return products
