# Problem Challenge 2: Comparing Strings containing Backspaces (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743506829_10Unit

# Problem Statement
#
# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.
#
# Example 1:
# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
#
# Example 2:
# Input: str1="xy#z", str2="xyz#"
# Output: false
# Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
#
# Example 3:
# Input: str1="xp#", str2="xyz##"
# Output: true
# Explanation: After applying backspaces the strings become "x" and "x" respectively.
# In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
#
# Example 4:
# Input: str1="xywrrmp", str2="xywrrmu#p"
# Output: true
# Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.

# Solution
#
# To compare the given strings, first, we need to apply the backspaces. An efficient way to do this would be from the
# end of both the strings. We can have separate pointers, pointing to the last element of the given strings. We can
# start comparing the characters pointed out by both the pointers to see if the strings are equal. If, at any stage,
# the character pointed out by any of the pointers is a backspace (’#’), we will skip and apply the backspace until
# we have a valid character available for comparison.

def backspace_compare(str1, str2):
    # use two pointer approach to compare the strings
    index1 = len(str1) - 1
    index2 = len(str2) - 1
    while index1 >= 0 or index2 >= 0:
        i1 = get_next_valid_char_index(str1, index1)
        i2 = get_next_valid_char_index(str2, index2)
        if i1 < 0 and i2 < 0:  # reached the end of both the strings
            return True
        if i1 < 0 or i2 < 0:  # reached the end of one of the strings
            return False
        if str1[i1] != str2[i2]:  # check if the characters are equal
            return False

        index1 = i1 - 1
        index2 = i2 - 1

    return True


def get_next_valid_char_index(str, index):
    backspace_count = 0
    while index >= 0:
        if str[index] == '#':  # found a backspace character
            backspace_count += 1
        elif backspace_count > 0:  # a non-backspace character
            backspace_count -= 1
        else:
            break

        index -= 1  # skip a backspace or a valid character

    return index


def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()
