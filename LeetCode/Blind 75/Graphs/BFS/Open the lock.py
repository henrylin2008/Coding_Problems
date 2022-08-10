# Open the Lock
# https://algo.monster/problems/open_the_lock

# You commissioned a locksmith to craft a special combination lock for you, because you are a lich and you want to
# hide your phylactery in somewhere secure. It looks like a regular 4-digit combination lock, with each digit can be
# one of the digits from 0~9. Each digit can be turned forwards by 1 and backwards by 1, and the first and the last
# digit is connected (9 goes to 0 when moving forward, and 0 goes to 9 when moving backward). The lock starts at 0000.
#
# However, because you don't want people to find your phylactery, you have trapped certain combinations of this
# combination lock. If someone were to set the combination to a trapped combination, bad things happen to them,
# which this question would not elaborate upon.
#
# You know the combination, and you know the trapped combinations. You wonder if the lock can be opened without
# triggering the traps, and if so, how many digit changes must be made to the lock to unlock it.
#
# Input
#   -target_combo: a string representing the four digit combination to open the lock.
#   -trapped_combos: a list of strings representing the trapped combinations.
#
# Output
# An integer representing the number of steps it takes to open the lock, or -1 if you can't open it without triggering
# the trap.
#
# Examples
# Example 1:
# Input:
#   1. target_combo = "0202"
#   1. trapped_combos = ["0201","0101","0102","1212","2002"]

# Output: 6
#
# Explanation:
# 0000 -> 1000 -> 1100 -> 1200 -> 1201 -> 1202 -> 0202, a total of 6 steps.
#
# Constraints
# The starting combination (0000) and the final combination is not trapped because that defeats the purpose of the lock.

# Solution
# This question is a standard BFS problem, except we consider two combinations who has one digit differ by one
# "adjacent". The implementation comes easily after we defined what "adjacent" means for this question.
#
# The time complexity is O(n), where n is the number of possible combinations (which is 10^4 == 10000 in this case).

from collections import deque
from typing import List

next_digit = {**{str(i): str(i + 1) for i in range(9)}, "9": "0"}
prev_digit = {e: n for n, e in next_digit.items()}


def num_steps(target_combo: str, trapped_combos: List[str]) -> int:
    if target_combo == "0000":
        return 0
    trapped_combo_set = set(trapped_combos)
    steps = {
        "0000": 0
    }
    bfs_queue = deque({"0000"})
    while bfs_queue:
        top = bfs_queue.popleft()
        for i in range(4):
            new_combo = top[0:i] + next_digit[top[i]] + top[i + 1:]
            if new_combo not in trapped_combo_set and new_combo not in steps:
                bfs_queue.append(new_combo)
                steps[new_combo] = steps[top] + 1
                if new_combo == target_combo:
                    return steps[new_combo]
            new_combo = top[0:i] + prev_digit[top[i]] + top[i + 1:]
            if new_combo not in trapped_combo_set and new_combo not in steps:
                bfs_queue.append(new_combo)
                steps[new_combo] = steps[top] + 1
                if new_combo == target_combo:
                    return steps[new_combo]
    return -1


if __name__ == '__main__':
    target_combo = input()
    trapped_combos = input().split()
    res = num_steps(target_combo, trapped_combos)
    print(res)
