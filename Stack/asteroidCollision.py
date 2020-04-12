# Asteroid Collision
# LeetCode 735: https://leetcode-cn.com/problems/asteroid-collision/
# We are given an array asteroids of integers representing asteroids in a row.
#
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning
# right, negative meaning left). Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both
# are the same size, both will explode. Two asteroids moving in the same direction will never meet.
#
# Example 1:
# Input:
# asteroids = [5, 10, -5]
# Output: [5, 10]
# Explanation:
# The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

# Example 2:
# Input:
# asteroids = [8, -8]
# Output: []
# Explanation:
# The 8 and -8 collide exploding each other.

# Example 3:
# Input:
# asteroids = [10, 2, -5]
# Output: [10]
# Explanation:
# The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.

# Example 4:
# Input:
# asteroids = [-2, -1, 1, 2]
# Output: [-2, -1, 1, 2]
# Explanation:
# The -2 and -1 are moving left, while the 1 and 2 are moving right.
# Asteroids moving the same direction never meet, so no asteroids will meet each other.

# Note:
#
# The length of asteroids will be at most 10000.
# Each asteroid will be a non-zero integer in the range [-1000, 1000]..
#

# Time: O(N); N is number of asteroid
# Space: O(N); where stack (ans) space
# Idea: if new item is > 0, push it to stack, b/c it will always going to the right and not gonna collide with last item
# if abs(new) < abs(last): remove new item
# if abs(new) == abs(last), remove both items
# if abs(new) > abs(last), remove last item (run in while loop to go through rest of values in the stack)

class Solution(object):
    def asteroidCollision(self, asteroids):
        ans = []
        for new in asteroids: # for each new item
            while ans and new < 0 < ans[-1]: # while there's ans stack, and new item is < 0 and last item > 0
                if ans[-1] < abs(new):   # if last item in stack < abs(new)
                    ans.pop() # remove last item in stack
                    continue
                elif ans[-1] == abs(new): # if last item in stack == abs(new):
                    ans.pop() # remove new and last item (as they collided in same size, ex: 5, -5)
                break
            else:
                ans.append(new) # add new item to the stack
        # print(ans)
        return ans

Solution.asteroidCollision(1, [5, 6, 7, -8])











