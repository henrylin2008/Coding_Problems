# Reorganize String
# https://algo.monster/problems/reorganize_string

# Given a string s, check if the letters can be rearranged so that two characters that are adjacent to each other are
# not the same.
#
# If possible, output any possible result. If not possible, return the empty string.
#
# Example 1:
# Input:s = "aab"
# Output: aba
# Example 2:
# Input:s = "aaab"
# Output: ``
# Note:
# s will consist of lowercase letters and have length in range [1, 500].

# Solution
# We divide the indices of the string into two: odds and evens. In that case, elements with odd indices can only be
# adjacent to elements with even indices, and vice versa. Note that because the index starts at zero, there will
# always be more or equal evens than odds. If there are more of one character than the number of evens,
# it is impossible to rearrange the string so no adjacent characters are the same. Otherwise, we can start from the
# character that occurs the most and fill out spots with even indices. Once we run out of spots to fill, we fill out
# the spots with odd indices. In this case, the result will guarantee to have no same adjacent characters.
#
# For the implementation, we use a heap to guarantee the character that is repeated the most is processed first,
# and because the character repeated the most changes as we process more characters.

from heapq import heapify, heappop
from typing import Counter


def reorganize_string(s: str) -> str:
    n = len(s)
    # Count up the characters that appear in the string
    str_count = Counter[s]
    # store negative value since we want a max heap
    pq = [(-value, key) for key, value in str_count.items()]
    heapify(pq)
    # Return empty string if there are too many of one character
    if - pq[0][0] > (n + 1) // 2:
        return ""
    # Stores the resulting char array to be converted to string
    res = [None] * n
    # Pointer to the next item to be inserted
    # Increment by 2 until it reaches the end to fill out even positions,
    # then it is reset to 1 to fill out odd positions
    pointer = 0
    # Insert characters into the char array by their multiplicity
    while len(pq) > 0:
        (count, char) = heappop(pq)
        count = - count
        for i in range(count):
            res[pointer] = char
            pointer += 2
            if pointer >= n:
                pointer = 1
    return "".join(res)


if __name__ == '__main__':
    s = input()
    res = reorganize_string(s)
    if not res:
        print("Impossible")
        exit()
    input_counter, output_counter = Counter[s], Counter[res]
    if input_counter != output_counter:
        print("Not rearrangement")
        exit()
    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            print(f"Same character at index {i} and {i + 1}")
            exit()
    print("Valid")
