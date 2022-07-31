# Decode Ways
# Link: https://algo.monster/problems/decode_ways

# We have a message to decode. Letters are encoded to digits by their positions in the alphabet
#
# 1 A -> 1
# 2 B -> 2
# 3 C -> 3
# 4 ...
# 5 Y -> 25
# 6 Z -> 26
#
# Given a non-empty string of digits, how many ways are there to decode it?
#
# Input: "18"
#
# Output: 2
#
# Explanation: "18" can be decoded as "AH" or "R"
#
# Input: "123"
#
# Output: 3
#
# Explanation: "123" can be decoded as "ABC", "LC", "AW"


# 1. Identify states
# What state do we need to know whether we have decoded a string?
#   1. We can keep track of the number of digits we have already matched in index i. When i == length of digits, we have
#   finished.
# What state do we need to decide which child nodes of the state-space tree should be visited next?
# Since there's no constraint on which letters can be used for decoding, we don't need any state here.
#
# 2. Draw the space-state tree
#                       123
#                1=A  /     \ 12=L
#                  23         3
#             2=B/   \23=w      \ 3=c
#              3      ''         ''
#               \ 3=c
#                ''
#
# 3. DFS
# Using the backtracking template as a basis, we add the state we identified in step 1:
#   1. i for the number of digits we have already matched.
#
# DFS returns the number of ways we can decode digits[i:].
#
# Time Complexity: O(2^n)
#
# n is the length of the string. Essentially at every digit we either make a new number or add it to the old one. We
# can make this into linear time through dp but currently we have a exponential time solution.

def decode_ways(digits):
    # use numbers 1 to 26 to represent all alphabet letters
    prefixes = [str(i) for i in range(1, 27)]

    def dfs(start_index):
        if start_index == len(digits):
            return 1

        ways = 0
        remaining = digits[start_index:]
        for prefix in prefixes:
            if remaining.startswith(prefix):
                ways += dfs(start_index + len(prefix))  # add number of ways returned from child node

        return ways

    return dfs(0)


# Again, we see there are overlapping subproblems.


# Add memoization:
def decode_ways(digits):
    prefixes = [str(i) for i in range(1, 27)]

    def dfs(start_index, memo):
        if start_index in memo:
            return memo[start_index]
        if start_index == len(digits):
            return 1
        ways = 0
        remaining = digits[start_index:]
        for prefix in prefixes:
            if remaining.startswith(prefix):
                ways += dfs(start_index + len(prefix), memo)
        memo[start_index] = ways
        return ways

    return dfs(0, {})
