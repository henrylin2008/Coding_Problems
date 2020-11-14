# Link: https://www.algoexpert.io/questions/Product%20Sum
# Product Sum:
# Write a function that takes in a "special" array and returns its product sum. A "special" array is a non-empty array
# that contains either integers or other "special" arrays. The product sum of a "special" array is the sum of its
# elements, where "special" arrays inside it should be summed themselves and then multiplied by their level of depth.
# For example, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2y + 2z.
# Sample input: [5,2,[7, - 1],3,[6,[-13,8],4]]
# Sample output: 12 (calculated as: (5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)))

# Time: O(n), n is total number of elements in the array, including sub-elements
# Space: O(d), d is the greatest depth of "special" arrays in the array
def productSum(array, multiplier=1):
    sums = 0
    for element in array:
        if type(element) is list:  # if element is a type of list
            sums += productSum(element, multiplier + 1)  # recursive call of productSum, add 1 to multiplier and add
            # to element
        else:
            sums += element
    # print(sum*multiplier)
    return sums * multiplier

# productSum([5,2,[7, - 1],3,[6,[-13,8],4],[10]])
