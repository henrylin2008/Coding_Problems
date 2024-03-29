# 207. Course Schedule
# Link:https://leetcode.com/problems/course-schedule/
# Medium

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
# prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So
# it is impossible.
#
#
# Constraints:
#
# 1 <= numCourses <= 105
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

# note: build adjacentcy_list with edges, run dfs on each V, if while dfs on V we see V again, then loop exists,
# otherwise V isnt in a loop, 3 states= not visited, visited, still visiting

# Idea: using a dictionary to store courses and map its prerequisites list, use a set to store visited courses, run dfs
# on the course, if any course from visited_set shows up again, which mean there's a loop, return False; then run dfs
# on the prerequisites, return False if any course can't be completed; then remove current course from the visited_ste,
# and set the prerequisite of the current course to empty and return True for dfs(course). Run a for loop on numCourses,
# if any of the course return False, return False;
from typing import List


# Time: O(n + pre); n: number of nodes; pre: prerequisites
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        pre_map = {i: [] for i in range(numCourses)}  # ex: [[1,0]] -> {0: [], 1: [0]}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visited_set = set()           # all courses along the current DFS path

        def dfs(crs):
            # base cases
            if crs in visited_set:    # if the course already been visited (visiting twice); there's a loop
                return False
            if pre_map[crs] == []:    # this course has no prereq
                return True

            visited_set.add(crs)      # add this crs to visit_set, currently visiting this course
            for pre in pre_map[crs]:  # loop through prereq for this course
                if not dfs(pre):      # run dfs on pre, if one course can't be completed, then return False
                    return False
            visited_set.remove(crs)   # remove current/visited crs from visited_set
            pre_map[crs] = []         # set no prereq on current visiting course
            return True

        for crs in range(numCourses):  # run dfs on every course; ex: courses are not connected; 1 -> 2; 3 -> 4
            if not dfs(crs):           # False if any dfs return false
                return False
        return True
