# Link: https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers
# # Find Three Largest Numbers
# # Write a function that takes in an array of integers and returns a sorted array of the three largest integers in the
# # input array. Note that the function should return duplicate integers if necessary; for example, it should return
# # [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
# # Sample input: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
# # Sample output: [18, 141, 541]

def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        calThreeLargest(threeLargest, num)  # helper method
    # print(threeLargest)
    return threeLargest

def calThreeLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]: # calculate last index value if it's None or num > [2]
        shiftUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]: # calculate 2nd index value if it's None or num > [1]
        shiftUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]: # calculate first index value if it's None or num > [0]
        shiftUpdate(threeLargest, num, 0)

def shiftUpdate(array, num, index):
    # Objective: if i == (last) index , then set the num = array[i] (array[2] in this case)
    # else: shift index one position to the left
    # [0, 1, 2]    ==>      [0, 1, 2]
    # [x, y, z]    ==>      [y, z, num]
    for i in range(index+1):
        if i == index:
            array[i] = num
        else:
            array[i] = array[i+1]


findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 183, 541, 988, 7, 7])