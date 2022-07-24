# Permutations
# Given a string of unique letters, find all of its distinct permutations.
#
# Input
# letters: a string of unique letters
# Output
# all of its distinct permutations
#
# Example 1:
# Input:
# letters = `abc`
# Output:
# ```` abc acb bac bca cab cba




# 3-step system from backtracking template:
# 1. Identify States
# What state do we need to know whether we have reached a solution (and using it to construct a solution if the problem
# asks for it)?
#   -We need a state to keep track of the list of letters we have chosen for the current permutation
# What state do we need to decide which child nodes should be visited next and which ones should be pruned?
#   -We have to know what are the letters left that we can still use (since each letter can only be used once)?
# 2. Draw the State-space Tree
# 3. DFS on the State-space tree
# Using the backtracking template as basis, we add the two states we identified in step 1:
#   -A path list to represent permutation constructed so far.
#   -A used list to record which letters are already used. used[i] == true means ith letter in the origin list has been
#    used.

from typing import List


# Time Complexity: O(n!)
# This is because we have n letters to choose from then n - 1 and so on therefore n * (n - 1) * (n - 2) * ... * 1
def permutations(letters):
    def dfs(path, used, res):
        if len(path) == len(letters):
            res.append(''.join(path))
            return

        for i, letter in enumerate(letters):
            # skip used letters
            if used[i]:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            used[i] = True
            dfs(path, used, res)
            # remove letter from permutation, mark letter as unused
            path.pop()
            used[i] = False

    res = []
    dfs([], [False] * len(letters), res)
    return res


if __name__ == '__main__':
    letters = input()
    res = permutations(letters)
    for line in res:
        print(line)
