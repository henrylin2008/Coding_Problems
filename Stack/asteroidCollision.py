# Asteroid Collision
# LeetCode 735: https://leetcode.com/problems/asteroid-collision/
# https://leetcode-cn.com/problems/asteroid-collision/
# Difficulty: Medium
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
#
# Idea: if new item is > 0, push it to stack, b/c it will always going to the right and not gonna collide with last item
# if abs(new) < res[last]: remove new item
# if abs(new) == res[last], remove both items
# if abs(new) > res[last], remove last item (in while loop to go through rest of values in the stack)
# append anything except abs(new) >= res[-1]

# 方法：栈
# 如果不会发生碰撞那么一排小行星是处于稳定的状态。若在右边增加一个新的小行星后，在它再次稳定之前，可能会发生更多的碰撞，而所有的这些碰撞（如果发生的话）
# 都必须从右到左发生。这种情况非常适合用栈解决。
#
# 算法：
#
# 假设栈中顶部元素为 top，一个新的小行星 new 进来了。如果 new 向右移动（new>0），或者 top 向左移动（top<0），则不会发生碰撞。
# 否则，如果 abs(new) < abs(top)，则新小行星 new 将爆炸；如果 abs(new) == abs(top)，则两个小行星都将爆炸；如果 abs(new) > abs(top)，
# 则 top 小行星将爆炸（可能还会有更多小行星爆炸，因此我们应继续检查）


class Solution(object):
    def asteroidCollision(self, asteroids):
        res = []
        for new in asteroids: # for each new item
            while res and new < 0 < res[-1]: # while there's res stack, and new item is < 0 and last item > 0
                if res[-1] < abs(new):   # if last item in stack < abs(new)
                    res.pop() # remove last item in stack
                    continue
                elif res[-1] == abs(new): # if last item in stack == abs(new):
                    res.pop() # remove new and last item (as they collided in same size, ex: 5, -5)
                break
            else:
                res.append(new) # add new item to the stack
        # print(res)
        return res

Solution.asteroidCollision(1, [5, 6, 7, -8])











