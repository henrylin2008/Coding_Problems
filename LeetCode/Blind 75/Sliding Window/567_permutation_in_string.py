# 567. Permutation in String
# Link: https://leetcode.com/problems/permutation-in-string/
# Medium

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
#
#
# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#
#
# Constraints:
#
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

class Solution:
    # Time: O(n)
    # Space: O(26); worse case to store all 26 lower case letters
    # Logic: use 2 arrays to keep track of count of each letter, and a variable (matches) to keep track of number of
    #        matched letters; use a sliding window to keep track of count of each letter, while moving the right
    #        pointer (adding count), shift the left pointer to the next position (decrement count); anytime when matches
    #        are equal to 26, then return True; if matches never reach 26, then return False
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False  # edge case

        s1_count, s2_count = [0] * 26, [0] * 26  # counts in the arrays; only 26 lower case letters
        for i in range(len(s1)):  # initialize 2 counts, up to len(s1)
            s1_count[ord(s1[i]) - ord('a')] += 1  # count of the letters, [ord(s1[i]) - ord('a')]: map the index
            s2_count[ord(s2[i]) - ord('a')] += 1
        matches = 0  # variable to keep track of matching letters
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)  # increment count by 1 if matches
        # sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True  # return True whenever matches == 26
            # following could be done with the hashmaps
            # adding the character on the right pointer
            idx = ord(s2[r]) - ord('a')  # index of s2_count array
            s2_count[idx] += 1  # increment count by 1
            if s1_count[idx] == s2_count[idx]:  # if count of same index matches
                matches += 1  # increment the matches
            elif s1_count[idx] + 1 == s2_count[idx]:  # s2_count >  s1_count; they were equal before s2_count[idx] += 1
                matches -= 1  # decrement the matches
            # removing the character from the left pointer
            idx = ord(s2[l]) - ord('a')  # index for left pointer
            s2_count[idx] -= 1  # remove char at the left pointer; decrement the count
            if s1_count[idx] == s2_count[idx]:  # if both counts are equal
                matches += 1  # increment by 1
            elif s1_count[idx] - 1 == s2_count[idx]:  # s1_count > s2_count
                matches -= 1  # decrement by 1
            l += 1  # shift left pointer
        return matches == 26  # True if matches == 26


#  similar logic as above: Use 2 hashmaps and sliding window to get the counts of each char, return True if the count
#  of the characters are the same within the range.
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s2) < len(s1):
#             return False
#         count_s1, count_s2 = {}, {}
#         for c in range(len(s1)):
#             count_s1[s1[c]] = 1 + count_s1.get(s1[c], 0)
#             count_s2[s2[c]] = 1 + count_s2.get(s2[c], 0)
#         if count_s1 == count_s2:
#             return True
#         l = 0
#         for r in range(len(s1), len(s2)):
#             count_s2[s2[r]] = 1 + count_s2.get(s2[r], 0)
#             count_s2[s2[l]] -= 1
#             if count_s2[s2[l]] == 0:
#                 count_s2.pop(s2[l])
#             l += 1
#             if count_s1 == count_s2:
#                 return True
#         return False
